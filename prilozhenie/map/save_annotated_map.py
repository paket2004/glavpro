import json
import cv2
import numpy as np

with open(r"prilozhenie/map/annotated_map_json/map_schema.json", "r") as f:
    data = json.load(f)

# image = cv2.imread(data["imagePath"])
image = cv2.imread('prilozhenie\map\screenshots\map_schema.jpg')
print("sth")
h, w = image.shape[:2]

labels = {}
for shape in data["shapes"]:
    label = shape["label"]
    if label not in labels:
        labels[label] = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))

for shape in data["shapes"]:
    points = np.array(shape["points"], dtype=np.int32)
    color = labels[shape["label"]]
    
    if shape["shape_type"] == "polygon":
        cv2.polylines(image, [points], isClosed=True, color=color, thickness=2)
    elif shape["shape_type"] == "rectangle":
        cv2.rectangle(image, tuple(points[0]), tuple(points[1]), color, 2)

legend_x = w - 200 
legend_y = 30
for i, (label, color) in enumerate(labels.items()):
    cv2.rectangle(image, (legend_x, legend_y + i*30), (legend_x + 20, legend_y + i*30 + 20), color, -1)
    cv2.putText(image, label, (legend_x + 30, legend_y + i*30 + 15), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

cv2.imwrite("prilozhenie/map/annotated_map/map_schema.jpg", image)
print("Изображение с легендой сохранено!")