r1.ipynb
merger.py
calc_merger
prilozhenie\prilozhenie2\generate_prilozhenie_2.py
prilozhenie\prilozhenie3\prilozhenie3.py
туп все py в tables
prilozhenie\prilozhenie5\prilozhenie5.py
streanlit run inn
переместить этот файлик в папку приложение 6
prilozhenie\prilozhenie6\prilozhenie6.py
prilozhenie\prilozhenie6\merger.py
потом get map, потом label me на эту картинку
сохранили, раним
активируем другой терминал
py -3.10 -m venv labelme_venv
labelme_venv/scripts/activate
pip install --upgrade labelme
pip install opencv-python numpy matplotlib  
pip install onnxruntime==1.15.1  
pip uninstall numpy 
 pip install "numpy<2.0"
pip install -r req2.txt  
labelme, открываем нашу картинку, размечаем ее, созраняем в папочку annotated_map_json с названием map_schema_annotated
python prilozhenie\map\save_annotated_map.py -> получаем картинку