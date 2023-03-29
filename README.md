# **ChillPlus Sorter**

## **What is this?**
This code snippets can help you to gather all the CHILL+ data that are separated into each frame files into one single file. If you are OVITO and CHILL+ plugin user, this code can help you to easily treat the data and plot the graph. 

## **How to use?**
1. Download this repository into your local machine. And then get into the folder.
    ```
    git clone https://github.com/wjgoarxiv/ChillPlus_sorter.git
    ```
    ```
    cd ChillPlus_sorter/
    ```

2. Bring the raw data folder that contains the frame files into the folder that you just cloned (Or remember the path of the folder). In the raw data folder, there might be files containing the CHILL+ analyses data obtained from the CHILL+ plugin in OVITO. For the detailed extraction method, please retrieve [THIS LINK](https://www.ovito.org/docs/current/reference/pipelines/modifiers/chill_plus.html#chill). 

3. Next, run `1_makecsv.py` in the terminal. You can run like this: 
    ```
    python3 1_makecsv.py -d [directory path of the raw data folder] -o [output CSV file name]
    ```
    There is demo raw folder in this repository. If you want to run `1_makecsv.py` with the demo folder, you can run like this:
    ```
    python3 ./src/1_makecsv.py -d ./GALLERY/Raw_chill+_files -o ./testoutput.csv
    ```
    If you need further information, you can retrieve the help message by running the following command:
    ```
    python3 ./src/1_makecsv.py -h
    ```

4. Assuming you worked with the demo raw folder and successfully ran the `1_makecsv.py`, you can obtain the `testoutput.csv` file. With this `.csv` file, you can easily plot the graph with the `2_plotgraph.py` script. You can run this file like this:
    ```
    python3 ./src/2_plotgraph.py -i ./testoutput.csv -o ./testoutput.png
    ```
    If you need further information, you can retrieve the help message by running the following command:
    ```
    python3 ./src/2_plotgraph.py -h
    ```

## **Gallery**
<img src = "">