import json
import os

class config_json:
    FILE_NAME = "config.json"

    def config(self):
        data = {
            "VNC_path": None,
            "PC_info": None,
            "data_filter": None
        }
        file_path = os.path.join(os.getcwd(), self.FILE_NAME)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            return True
        else:
            return False
#======================================================================
#       Json config file for VNC path    
# ========================================================================

    def update_VNC_path(self, path):
        file_path = os.path.join(os.getcwd(), self.FILE_NAME)
        with open(file_path, 'r+') as file:
            data = json.load(file)
            data["VNC_path"] = path  # Luôn cập nhật
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
            return True

    def get_VNC_path(self):
        file_path = os.path.join(os.getcwd(), self.FILE_NAME)
        with open(file_path, 'r') as file:
            data = json.load(file)
            if "VNC_path" in data:
                return True, data["VNC_path"]
            else:
                return False, None
    
#======================================================================
#      Json config file for PC info
# ========================================================================
    def add_PC_info(self, IP_address, pwd_vnc, Model,Station, Line):
        if self.check_info_PC_before_add(IP_address):
            print(f'IP {IP_address} already exists')
            return False
        info_pc = {
            "IP_PC": IP_address,
            "Pwd_VNC": pwd_vnc,
            "Model":Model,
            "Station": Station,
            "Line": Line
        }
        file_path = os.path.join(os.getcwd(), self.FILE_NAME)
        
        with open(file_path, 'r+') as file:
            data = json.load(file)
            
            if "PC_info" not in data or data["PC_info"] is None:
                data["PC_info"] = []

            data["PC_info"].append(info_pc)

            # GHI LẠI FILE SAU KHI THÊM MỚI
            file.seek(0)           # Di chuyển con trỏ về đầu file
            json.dump(data, file, indent=4)
            file.truncate()        # Xóa phần cũ nếu có

            return True

    def check_info_PC_before_add(self, IP_address):
        file_path = os.path.join(os.getcwd(), self.FILE_NAME)
        with open(file_path, 'r') as file:
            data = json.load(file)
            if "PC_info" in data and isinstance(data["PC_info"], list):
                for pc in data["PC_info"]:
                    if pc.get("IP_PC") == IP_address:
                        return True  # Đã tồn tại IP này
            return False  # Không tìm thấy IP này
        
    def find_info(self, data_search):
        file_path = os.path.join(os.getcwd(), self.FILE_NAME)
        result = []

        try:
            with open(file_path, "r") as file:
                data = json.load(file)

            pc_list = data.get("PC_info", [])
            if not isinstance(pc_list, list):
                return result

            for pc in pc_list:
                if (
                    data_search.lower() in pc.get("IP_PC", "").lower() or
                    data_search.lower() in pc.get("Pwd_VNC", "").lower() or
                    data_search.lower() in pc.get("Model", "").lower() or
                    data_search.lower() in pc.get("Station", "").lower() or
                    data_search.lower() in pc.get("Line", "").lower()
                ):
                    result.append(pc)

        except FileNotFoundError:
            print(f"File {file_path} không tồn tại.")
        except json.JSONDecodeError:
            print(f"Lỗi định dạng JSON trong file {file_path}.")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")

        return result

class main:
    def __init__(self):
        self.check_json()
        # self.add_PC_info("192.168.2.5", "password1234","SAR9","Station2", "LineB")
        self.find_pc("LineB")
    def check_json(self):
        config = config_json()
        if config.config():
            print("Config file is ready.")
        else:
            print("Config file already exists.")

    def update_VNC_path(self, path):
        config = config_json()
        if config.update_VNC_path(path):
            print(f"VNC path updated to: {path}")
        else:
            print("Failed to update VNC path.")
    def add_PC_info(self, IP_address, pwd_vnc, Model,Station, Line):
        config = config_json()
        if config.add_PC_info(IP_address, pwd_vnc, Model, Station, Line):
            print(f"PC info added: {IP_address}, {pwd_vnc}, {Model}, {Station}, {Line}")
        else:
            print("Failed to add PC info.")
    
    def find_pc(self, keyword):
        config = config_json()
        result =config.find_info(keyword)
        print(result)



if __name__ == "__main__":
    main()