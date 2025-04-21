from main import *
import time
import cv2

import os
import numpy as np

from io import BytesIO
from PIL import Image
from PySide6.QtCore import QObject, Signal, Slot
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image as ReportLabImage, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

class ReportingManager(QObject):
    finished = Signal(str)

    def __init__(self, workspace_path):
        super().__init__()
        self.report = {
            "test_cases":[],
            "execution_summary": {
                "total": 0,
                "passed": 0,
                "failed": 0,
                "blocked": 0,
                "total_execution_time": "",
            }
        }
        self.curr_test_id = ""
        self.curr_test_description = ""
        self.reportid = ""
        self.reportReady = False
        self.curr_test_start_time = None
        self.validation_failed_img = {}
        self.start_time = time.time()
        self.workspace = workspace_path

    @Slot(object,object,object)
    def compare_screens(self,diff,expected_image,current_image_rgb):
        """Placeholder function for screenshot validation."""
        print("🖼️ Comparing screenshots for report...")
        test_case_id = self.curr_test_id

        current_image  = cv2.cvtColor(current_image_rgb, cv2.COLOR_RGB2BGR)


        diff = (diff * 255).astype("uint8")
        #diff_box = cv2.merge([diff, diff, diff])

        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]

        for c in contours:
            area = cv2.contourArea(c)
            if area > 40:
                x,y,w,h = cv2.boundingRect(c)
                cv2.rectangle(expected_image, (x, y), (x + w, y + h), (36,255,12), 2)
                cv2.rectangle(current_image, (x, y), (x + w, y + h), (36,255,12), 2)

        self.store_failed_screenshots(test_case_id,expected_image,current_image)
        #self.validation_failed_img.append(expected_image)
        #self.validation_failed_img.append(current_image)

    @Slot(str,str)
    def test_started(self,test_case_id, description):
        print("report worker started")
        print(self.report)
        self.curr_test_start_time = time.time()
        self.curr_test_id = test_case_id
        self.curr_test_description = description

    @Slot(str,str,str)
    def write_report(self,test_case_id,status,error_message=""):
        
        execution_time = f"{int(time.time() - self.curr_test_start_time)}s"  # Calculate time taken per test
        
        if not test_case_id == self.curr_test_id:
            print("Error: the test case id not matching")
            return
        
        test_case_entry = {
            "id": self.curr_test_id,
            "description": self.curr_test_description,
            "status": status,
            "execution_time": execution_time,
            "error": error_message if status == "Failed" else "",
        }

        self.curr_test_id = ""

        self.report["test_cases"].append(test_case_entry)

        self.report["execution_summary"]["total"] += 1
        if status == "Passed":
            self.report["execution_summary"]["passed"] += 1
        elif status == "Failed":
            self.report["execution_summary"]["failed"] += 1
        else:
            self.report["execution_summary"]["blocked"] += 1

        print("report worker write report")
        print(self.report)

    @Slot()
    def finalize_report(self):
        """Finalizes execution time and exports the report."""
        if self.curr_test_id != "":
            self.write_report(self.curr_test_id,"Unkown","Unkown Error - cannot fetch details")
        total_time = int(time.time() - self.start_time)
        minutes, seconds = divmod(total_time, 60)
        hours, minutes = divmod(minutes, 60)
        self.report["execution_summary"]["total_execution_time"] = f"{hours}h {minutes}m {seconds}s"

        print("report worker finalize report")
        print(self.report)
        self.reportReady = True

        filename = ""
        self.reportid = f"{datetime.today().strftime('%Y%m%d%H%M')}"

        if(len(self.report["test_cases"])):
            filename = os.path.join(self.workspace, f"TestReport - {self.reportid}.pdf")
            self.gather_report(filename)

        time.sleep(5)

        self.finished.emit(filename)
    
    @Slot()
    def stop(self):
        self.finished.emit("")

    def store_failed_screenshots(self,test_case_id,expected_image,actual_image):
        #self.validation_failed_img[test_case_id] = [expected_image,actual_image]
        """Store screenshots in order for the same test case ID."""
        if test_case_id not in self.validation_failed_img:
            self.validation_failed_img[test_case_id] = []
        
        # Append the new screenshot pair in order
        self.validation_failed_img[test_case_id].append((expected_image, actual_image))

    def get_failed_screenshots(self, test_case_id):
        return self.validation_failed_img.get(test_case_id, [])

    def gather_report(self, output_file):
        """Generate a test report PDF from execution results."""
        doc = SimpleDocTemplate(
                                output_file,
                                pagesize=letter,
                                rightMargin=40,
                                leftMargin=40,
                                topMargin=60,
                                bottomMargin=40
                            )
        
        elements = []
        styles = getSampleStyleSheet()

        # Report Title
        elements.append(Paragraph(f"Test Report: {self.reportid}", styles["Title"]))
        elements.append(Spacer(1, 12))

        # Execution Summary
        summary = self.report["execution_summary"]
        summary_data = [
            ["Total Test Cases", summary["total"]],
            ["Passed", summary["passed"]],
            ["Failed", summary["failed"]],
            ["Blocked", summary["blocked"]],
            ["Total Execution Time", summary["total_execution_time"]],
        ]
        table = Table(summary_data, hAlign="LEFT", colWidths=[150, 70])
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.black),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            #("ALIGN", (0, 0), (-1, -1), "LEFT"),  # Ensure all cells are left-aligned
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.lightgrey),
        ]))
        elements.append(Paragraph("Execution Summary:", styles["Heading2"]))
        elements.append(table)
        elements.append(Spacer(1, 12))

        """elements.append(Paragraph(f"Report Prepared on         :{datetime.today().strftime('%m/%d/%Y - %H:%M')}", styles["BodyText"]))
        elements.append(Paragraph(f"Total Test Cases           :{summary["total"]}", styles["BodyText"]))
        elements.append(Paragraph(f"Passed                     :{summary["passed"]}", styles["BodyText"]))
        elements.append(Paragraph(f"Failed                     :{summary["failed"]}", styles["BodyText"]))
        elements.append(Paragraph(f"Blocked                    :{summary["blocked"]}", styles["BodyText"]))
        elements.append(Paragraph(f"Total Execution Time       :{summary["total_execution_time"]}", styles["BodyText"]))
        elements.append(PageBreak())"""
        normal_style = styles["Normal"]
        # Test Case Details Table
        data = [["Test Case ID", "Description", "Execution Time", "Status", "Error Message"]]
        for test in self.report["test_cases"]:
            row = [
                test["id"],
                Paragraph(test["description"],normal_style),
                test["execution_time"],
                test["status"],
                Paragraph(test["error"] if test["status"] == "Failed" else "-",normal_style)
            ]
            data.append(row)

        table = Table(data, hAlign="LEFT", colWidths=[90, 150, 80, 70, 150])
        t_style = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.black),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),  # Ensure all cells are left-aligned
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ('FONTSIZE', (0,0), (-1,0), 10),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ("BACKGROUND", (0, 1), (-1, -1), colors.lightgrey),
        ])

        for i, row in enumerate(data[1:], start=1):
            status = row[3].strip().lower()
            if status == "passed":
                bg_color = colors.lightgreen
            elif status == "failed":
                bg_color = colors.lightcoral
            elif status == "blocked":
                bg_color = colors.lightyellow
            else:
                bg_color = colors.white
            t_style.add('BACKGROUND', (3, i), (3, i), bg_color)
        table.setStyle(t_style)

        elements.append(Spacer(1,12))
        elements.append(Paragraph("Test Case Execution Details:", styles["Heading2"]))
        elements.append(table)
        elements.append(PageBreak())

        # Failed Test Case Screenshots
        for test in self.report["test_cases"]:
            if test["status"] == "Failed":
                elements.append(Paragraph(f"Failed Test: {test['id']} - {test['description']}", styles["Heading3"]))
                elements.append(Paragraph(f"Error: {test['error']}", styles["BodyText"]))
                self.add_images(test['id'], elements)

        # Generate PDF
        doc.build(elements)

    def convert_cv2_to_reportlab_image(self,opencv_image, width=200, height=130):
        """Convert OpenCV image (NumPy array) to ReportLab Image."""
        color_img = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(color_img)
        img_buffer = BytesIO()
        pil_image.save(img_buffer, format="PNG")
        img_buffer.seek(0)
        return ReportLabImage(img_buffer, width, height)
    
    def add_images(self,test_case_id,elements):
        """Add all screenshot pairs for the given test case ID to the elements list."""
        Images = self.get_failed_screenshots(test_case_id)

        if not Images:  # If no images found, return
            return

        for idx, (expected_img, actual_img) in enumerate(Images, start=1):
            # Convert images to reportlab format
            expected = self.convert_cv2_to_reportlab_image(expected_img)
            actual = self.convert_cv2_to_reportlab_image(actual_img)

            # Create a table with the screenshots
            data = [
                [f"Expected Screenshot Step:{idx}:", f"Actual Screenshot Step:{idx}:"],
                [expected, actual]
            ]
            table = Table(data, hAlign="LEFT", colWidths=[220, 220])

            table.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),  
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                ("GRID", (0, 0), (-1, -1), 1, colors.white)
            ]))

            # Add table and spacing to the elements list
            elements.append(Spacer(1, 12))
            elements.append(table)
            elements.append(Spacer(1, 12))
    
