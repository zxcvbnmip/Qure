import os
import json

# 获取所有文件名
directory_path = "IconSet/Color"
base_url = "https://raw.githubusercontent.com/Koolson/Qure/master/IconSet/Color/"

# 创建 icons 列表
icons = [{"name": f, "url": f"{base_url}{f}"} for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

# 构建最终的 JSON 数据结构
data = {
    "name": "Qure Color (All)",
    "icons": icons,
    "description": "Qure Color (All) 是 Qure 项目下的彩色主题的「所有」图标集 @Koolson"
}

# 确保 ./other 文件夹存在
output_directory = "./Other"
os.makedirs(output_directory, exist_ok=True)

# 将数据写入 icon.json 文件
with open(os.path.join(output_directory, "icon.json"), "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("JSON 数据已成功写入 ./other/icon.json")
