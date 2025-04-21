from main import *

class TestCaseManager:
    def __init__(self):
        self.list_test_cases = []

    def add_test_case(self, test_case):
        if self.get_test_case(test_case.test_case_id) is None:
            self.list_test_cases.append(test_case)
        return test_case.test_case_id
    
    def get_all_test_cases(self):
        return self.list_test_cases
    
    def get_test_case(self, test_case_id):
        return next((tc for tc in self.list_test_cases if tc.test_case_id == test_case_id), None)

    def update_test_case_status(self, test_case_id, status):
        test_case = self.get_test_case(test_case_id)
        if test_case:
            test_case.status = status

    def update_test_case_steps(self, test_case_id, steps):
        test_case = self.get_test_case(test_case_id)
        if test_case:
            test_case.steps = steps if isinstance(steps, list) else steps.split("\n")
    
    def remove_test_case(self, test_case_id):
        test_case = self.get_test_case(test_case_id)
        if test_case:
            self.list_test_cases.remove(test_case)

    def update_test_case(self, test_case_id, updated_test_case):
        #Updates an existing test case with the provided updated_test_case.
        for index, test_case in enumerate(self.list_test_cases):
            if test_case.test_case_id == test_case_id:
                self.list_test_cases[index] = updated_test_case
                return
        print(f"⚠️ Test case with ID {test_case_id} not found.")

    def load_test_case(self, test_case_id, bload):
        test_case = self.get_test_case(test_case_id)
        if test_case:
            test_case.bloaded = bload
        
    def get_loaded_test_cases(self):
        return [tc for tc in self.list_test_cases if tc.bloaded]
    
    def get_unloaded_test_cases(self):
        return [tc for tc in self.list_test_cases if not tc.bloaded]
    
    def update_test_case_repeat(self,test_case_id):
        test_case = self.get_test_case(test_case_id)
        if test_case:
            test_case.repeat += 1
    def reset_test_case_repeat(self,test_case_id):
        test_case = self.get_test_case(test_case_id)
        if test_case:
            test_case.repeat = 1

    def update_test_case_path(self, test_case_id, path):
        test_case = self.get_test_case(test_case_id)
        if test_case:
            test_case.strSourcePath = path

    def __repr__(self):
        return f"TestCaseManager({len(self.list_test_cases)} test cases)"

class TestCase:
    def __init__(self, test_case_id, description, steps, status="Pending"):
        self.test_case_id = test_case_id
        self.description = description
        self.steps = steps if isinstance(steps, list) else [] if steps is None else steps.split("\n")
        self.status = status
        self.bloaded = False
        self.strSourcePath = ""
        self.repeat = 1

    def __repr__(self):
        return f"TestCase({self.test_case_id}, {self.description}, {self.status})"
    
    def to_dict(self):
        #Returns the test case as a dictionary
        return {
            "TestCaseID": self.test_case_id,
            "TestCaseDescription": self.description,
            "TestCaseSteps": self.steps,
        }
    
    def load_test_case(self, test_case_path):
        #Loads a test case from a JSON file.
        if not os.path.exists(test_case_path):
            print(f"⚠️ Test case file not found at {test_case_path}!")
            return None

        with open(test_case_path, "r") as file:
            try:
                test_case_file = json.load(file)
            except json.JSONDecodeError:
                print("❌ Error: Invalid JSON format in test case file.")
                return None

        self.test_case_id = test_case_file.get("TestCaseID", "")
        self.description  = test_case_file.get("TestCaseDescription", "")
        self.steps        = test_case_file.get("TestCaseSteps", [])
        self.status       = test_case_file.get("Status", "Pending")

        return test_case_file
    
    def update_test_case(self, test_casefile_path, new_description=None, new_steps=None, new_status=None):
        #Updates a test case with new values.
        test_case = self.load_test_case(test_casefile_path)
        
        if test_case is None:
            return

        if new_description is not None:
            test_case["TestCaseDescription"] = new_description
            self.description = new_description
        if new_steps is not None:
            test_case["TestCaseSteps"] = new_steps if isinstance(new_steps, list) else new_steps.split("\n")
            self.steps = new_steps if isinstance(new_steps, list) else new_steps.split("\n")
        if new_status is not None:
            test_case["Status"] = new_status
            self.status = new_status

        folderpath = os.path.dirname(test_casefile_path)
        if folderpath:
            self.strSourcePath = folderpath

        with open(test_casefile_path, "w") as file:
            json.dump(test_case, file, indent=4)

        print(f"✅ Test case {self.test_case_id} updated successfully!")
