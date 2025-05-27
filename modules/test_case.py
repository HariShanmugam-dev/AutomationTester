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

    def __repr__(self):
        return f"TestCaseManager({len(self.list_test_cases)} test cases)"

class TestCase:
    def __init__(self, test_case_config,steps=[]):
        self.test_case_id = test_case_config.test_case_id
        self.description = test_case_config.description
        self.steps = steps
        self.status = "Pending"
        self.bloaded = False
        self.target_application_path = test_case_config.target_application_path
        self.cli_params = test_case_config.cli_params
        self.timer = test_case_config.timer
        self.auto_connect = test_case_config.auto_connect
        self.priority = test_case_config.priority
        self.asset_ids = test_case_config.asset_ids
        self.asset_path = test_case_config.asset_path

    def __repr__(self):
        return f"TestCase({self.test_case_id}, {self.description}, {self.status})"
    
    def to_dict(self):
        #Returns the test case as a dictionary
        return {
            "TestCaseID": self.test_case_id,
            "TestCaseDescription": self.description,
            "TargetApplicationPath": self.target_application_path,
            "CLIParams": self.cli_params,
            "Timer": self.timer,
            "AutoConnect": self.auto_connect,
            "Priority": self.priority,
            "AssetPath": self.asset_path,
            "AssetIds": self.asset_ids,
            "TestCaseSteps": self.steps
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
        self.target_application_path = test_case_file.get("TargetApplicationPath", "")
        self.cli_params   = test_case_file.get("CLIParams", "")
        self.timer        = test_case_file.get("Timer", 0)
        self.auto_connect  = test_case_file.get("AutoConnect", False)
        self.priority     = test_case_file.get("Priority", 0)
        self.asset_path   = test_case_file.get("AssetPath", "")
        self.asset_ids    = test_case_file.get("AssetIds", [])
        self.bloaded      = False
        self.status       = "Pending"


        return test_case_file
    
    def update_test_case(self, test_casefile_path, **kwargs):
        """
        Updates a test case file with new values for any provided fields.
        Acceptable kwargs: TestCaseID, TestCaseDescription, TestCaseSteps, 
                        TargetApplicationPath, CLIParams, Timer, AutoConnect, 
                        Priority, AssetIds
        call like this:
            self.update_test_case(
            "path/to/testcase.json",
            TestCaseDescription="Updated description",
            CLIParams="--new-param",
            Timer=15,
            AutoConnect=True,
            TestCaseSteps="Step 1\nStep 2\nStep 3"
        )
        """
        test_case = self.load_test_case(test_casefile_path)
        if test_case is None:
            print(f"❌ Test case at {test_casefile_path} not found.")
            return

        # Map of field names to instance variable names for auto-updating instance state
        field_mapping = {
            "TestCaseID": "test_case_id",
            "TestCaseDescription": "description",
            "TargetApplicationPath": "target_application_path",
            "CLIParams": "cli_params",
            "Timer": "timer",
            "AutoConnect": "auto_connect",
            "Priority": "priority",
            "AssetPath": "asset_path",
            "AssetIds": "asset_ids",
            "TestCaseSteps": "steps",
        }

        for key, value in kwargs.items():
            if key in field_mapping:
                # Special handling for TestCaseSteps if string
                if key == "TestCaseSteps" and isinstance(value, str):
                    value = value.split("\n")
                setattr(self, field_mapping[key], value)

        with open(test_casefile_path, "w") as file:
            json.dump(test_case, file, indent=4)

        print(f"✅ Test case {test_case.get('TestCaseID', 'unknown')} updated successfully!")


class TestCaseConfig:
    def __init__(self, test_case_id="", description="", target_application_path="", cli_params="", timer=0, auto_connect=False, priority=0, asset_path="",asset_ids=None):
        self.test_case_id = test_case_id
        self.description = description
        self.target_application_path = target_application_path
        self.cli_params = cli_params
        self.timer = timer
        self.auto_connect = auto_connect
        self.priority = priority
        self.asset_path = asset_path
        self.asset_ids = asset_ids or []

    def to_dict(self):
        return {
            "TestCaseID": self.test_case_id,
            "TestCaseDescription": self.description,
            "TargetApplicationPath": self.target_application_path,
            "CLIParams": self.cli_params,
            "Timer": self.timer,
            "AutoConnect": self.auto_connect,
            "Priority": self.priority,
            "AssetPath": self.asset_path,
            "AssetIds": self.asset_ids
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            test_case_id=data.get("TestCaseID", ""),
            description=data.get("TestCaseDescription", ""),
            target_application_path=data.get("TargetApplicationPath", ""),
            cli_params=data.get("CLIParams", ""),
            timer=data.get("Timer", 0),
            auto_connect=data.get("AutoConnect", False),
            priority=data.get("Priority", "LOW"),
            asset_path=data.get("AssetPath", ""),
            asset_ids=data.get("AssetIds", [])
        )


class WorkspaceManager:
    def __init__(self):
        self.strWorkspaceName = ""
        self.strWorkspacePath = ""
        self.strTargetApplicationPath = ""
        self.strCLIparams = ""
        self.strReportsPath = ""
        self.strsetupScriptPath = ""
        self.strcleanupScriptPath = ""
        self.bautoConnect = False
        self.issTimer = 0;
        self.bautoload = False
        self.strAssetsPath = ""
        self.testCases = []
    # --- Getter and Setter for strWorkspaceName ---
    def get_workspace_name(self):
        return self.strWorkspaceName

    def set_workspace_name(self, name):
        self.strWorkspaceName = name

    # --- Getter and Setter for strWorkspacePath ---
    def get_workspace_path(self):
        return self.strWorkspacePath

    def set_workspace_path(self, path):
        self.strWorkspacePath = path

    # --- Getter and Setter for strTargetApplicationPath ---
    def get_target_application_path(self):
        return self.strTargetApplicationPath

    def set_target_application_path(self, path):
        self.strTargetApplicationPath = path

    # --- Getter and Setter for strCLIparams ---
    def get_cli_params(self):
        return self.strCLIparams

    def set_cli_params(self, params):
        self.strCLIparams = params

    # --- Getter and Setter for strReportsPath ---
    def get_reports_path(self):
        return self.strReportsPath

    def set_reports_path(self, path):
        self.strReportsPath = path

    # --- Getter and Setter for strAssetsPath ---
    def get_assets_path(self):
        return self.strAssetsPath
    def set_assets_path(self, path):
        self.strAssetsPath = path

    # --- Getter and Setter for strsetupScriptPath ---
    def get_setup_script_path(self):
        return self.strsetupScriptPath

    def set_setup_script_path(self, path):
        self.strsetupScriptPath = path

    # --- Getter and Setter for strcleanupScriptPath ---
    def get_cleanup_script_path(self):
        return self.strcleanupScriptPath

    def set_cleanup_script_path(self, path):
        self.strcleanupScriptPath = path

    # --- Getter and Setter for bautoConnect ---
    def get_auto_connect(self):
        return self.bautoConnect

    def set_auto_connect(self, flag):
        self.bautoConnect = flag

    # --- Getter and Setter for issTimer ---
    def get_ss_timer(self):
        return self.issTimer

    def set_ss_timer(self, timer_value):
        self.issTimer = timer_value

    # --- Getter and Setter for bautoload ---
    def get_auto_load(self):
        return self.bautoload

    def set_auto_load(self, flag):
        self.bautoload = flag

    # --- Getter and Setter for testCases ---
    def get_test_cases(self):
        return self.testCases
    
    def set_test_cases(self, test_cases):
        if isinstance(test_cases, list):
            self.testCases = test_cases
        else:
            raise ValueError("testCases should be a list of TestCase objects.")
    
    def add_test_case(self, test_case):
        if isinstance(test_case, TestCaseConfig):
            self.testCases.append(test_case)
            self.update_to_file()

    def clear(self):
        """Reset all workspace properties to their default values."""
        self.strWorkspaceName = ""
        self.strWorkspacePath = ""
        self.strTargetApplicationPath = ""
        self.strCLIparams = ""
        self.strReportsPath = ""
        self.strsetupScriptPath = ""
        self.strcleanupScriptPath = ""
        self.bautoConnect = False
        self.issTimer = 0
        self.bautoload = False

    def load_from_file(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Workspace config file not found: {filepath}")

        with open(filepath, 'r') as file:
            data = json.load(file)

        self.strWorkspaceName = data.get("WorkspaceName", "")
        self.strWorkspacePath = data.get("WorkspacePath", "")
        self.strTargetApplicationPath = data.get("TargetApplicationPath", "")
        self.strCLIparams = data.get("CLIparams", "")
        self.strReportsPath = data.get("ReportsPath", "")
        self.strAssetsPath = data.get("AssetsPath", "")
        self.strsetupScriptPath = data.get("SetupScriptPath", "")
        self.strcleanupScriptPath = data.get("CleanupScriptPath", "")
        self.bautoConnect = data.get("AutoConnect", False)
        self.issTimer = data.get("SsTimer", 0)
        self.bautoload = data.get("Autoload", False)
        self.testCases = [TestCaseConfig.from_dict(tc) for tc in data.get("TestCases", [])]


    def get_project_folder_path(self):
        project_location = self.strWorkspacePath.strip()
        project_name = self.strWorkspaceName.strip()
        path = os.path.join(project_location, project_name)
        path = os.path.normpath(path)  # Normalize the path
        return path
    
    def save_to_file(self):
        project_folder = self.get_project_folder_path()
        data = {
            "WorkspaceName": self.strWorkspaceName,
            "WorkspacePath": project_folder,
            "TargetApplicationPath": self.strTargetApplicationPath,
            "CLIparams": self.strCLIparams,
            "ReportsPath": self.strReportsPath,
            "AssetsPath": self.strAssetsPath,
            "SetupScriptPath": self.strsetupScriptPath,
            "CleanupScriptPath": self.strcleanupScriptPath,
            "AutoConnect": self.bautoConnect,
            "SsTimer": self.issTimer,
            "Autoload": self.bautoload,
            "TestCases": [tc.to_dict() for tc in self.testCases]
        }

        
        try:
            os.makedirs(project_folder, exist_ok=True)

            file_path = os.path.join(project_folder, f"{data['WorkspaceName']}.atest")

            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)

            return True, file_path

        except Exception as e:
            print(f"Error saving workspace config: {e}")
            return False, None
    
    def update_to_file(self):

        data = {
            "WorkspaceName": self.strWorkspaceName,
            "WorkspacePath": self.strWorkspacePath,
            "TargetApplicationPath": self.strTargetApplicationPath,
            "CLIparams": self.strCLIparams,
            "ReportsPath": self.strReportsPath,
            "AssetsPath": self.strAssetsPath,
            "SetupScriptPath": self.strsetupScriptPath,
            "CleanupScriptPath": self.strcleanupScriptPath,
            "AutoConnect": self.bautoConnect,
            "SsTimer": self.issTimer,
            "Autoload": self.bautoload,
            "TestCases": [tc.to_dict() for tc in self.testCases]
        }

        
        try:

            file_path = os.path.join(self.strWorkspacePath, f"{data['WorkspaceName']}.atest")

            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)

            return True, f"Settings updated at: {file_path}"

        except Exception as e:
            return False, str(e)
        
    def rename_workspace(self, new_workspace_name):
        old_file_path = os.path.join(self.strWorkspacePath, f"{self.strWorkspaceName}.atest")
        new_file_path = os.path.join(self.strWorkspacePath, f"{new_workspace_name}.atest")

        try:
            # Rename the .atest file if the name is changing and file exists
            if self.strWorkspaceName != new_workspace_name and os.path.exists(old_file_path):
                os.rename(old_file_path, new_file_path)

            # Update workspace name
            self.strWorkspaceName = new_workspace_name

            # Update the content of the .atest file to reflect new name
            success, message = self.update_to_file()

            if not success:
                return False, message

            return True, f"settings file successfully updated."

        except Exception as e:
            return False, str(e)
        
    def delete_test_case(self, test_case_id):
        try:
            # Find the test case object
            test_case_to_remove = next((tc for tc in self.testCases if tc.test_case_id == test_case_id), None)

            if test_case_to_remove:
                #remove the test case file from the workspace
                pathname = os.path.join(self.get_workspace_path()+"/testcases",f"{test_case_to_remove.test_case_id}.json")
                if os.path.exists(pathname):
                    os.remove(pathname)
                else:
                    return False, f"Test case file '{pathname}' does not exist."
                # remove assets from the workspace
                assetpath = test_case_to_remove.asset_path
                for asset in test_case_to_remove.asset_ids:
                    filepath = os.path.join(assetpath, asset)
                    if os.path.exists(filepath):
                        os.remove(filepath)
                # Remove it from the list
                self.testCases.remove(test_case_to_remove)

                # Update the workspace file
                success, message = self.update_to_file()

                if success:
                    return True, f"Test case '{test_case_id}' removed successfully."
                else:
                    return False, f"Test case removed but failed to update file: {message}"
            else:
                return False, f"Test case '{test_case_id}' not found."

        except Exception as e:
            return False, str(e)
        
    def get_test_case_config(self, test_case_id):
        return next((tc for tc in self.test_cases if tc.test_case_id == test_case_id), None)
    
