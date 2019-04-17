# FYP_2019
This is the Final year project of TAO Shenglan, Hong Kong Baptist University, in 2019. This work focus on the data summarized visualization for DAG data. The work is greatly based on by a theory published on the short paper Ontology-based Graph Visualization for Summarized View by Dr. Xin Huang et al., but not for a tree, this work change the original method from only suitable for tree to suitable for both tree and DAG.

=========How to use it========
1. Download the Java Web project "test" and import it into your Eclipse Java EE IDE, download the code folder.
2. Set the path in /code/source.cpp:
  [1] Change the source file path to your local path(input relationships bewteen the nodes, frequency of the nodes, name of the nodes(with ID);
  [2] Change the output file path to where you want;
  [3] Save the file and compile it by using GUN (i.e. g++ source.cpp)
3. Set the path in Web project "test":
  [1] In /src: Change the file path in "HelloServlet.java" and "UpdateServlet.java"
  [2] Change the file path in Anaylsis.jsp
4. If you have your own dataset, please translate it into the required format( You can use the DAG_count.py, Change_into_IDandFreq.py and Ori-GraphAnalysis.py in /test/WebContent to modify and analysis your dataset.)
5. Start the Web project in Eclipse, then use Chrome/FireFox to open the index page.
6. Follow the instruction on the website.

=========Input and Output========
1. files for source.cpp:
  [1] Input: rela_for_kvdo_Japan.txt, freq_Japan.txt, name_and_ID.csv: relationships, freqency and name of the dataset.
  [2] Output: dag-result.csv, ScoreResult.csv: selected data and evaluation result of the algorithm.
2. files for web project:
  [1] rela_with_freq_Japan_ALL.csv: the source file for DAG graph.
  [2] dag-result: the source  file for summarized DAG graph.
  [3] anal_table_Japan.csv: source file for Anaylsis_0.jsp and Anaylsis.jsp.
  [4] ScoreResult.csv: source file for Anaylsis.jsp.
  
  ------------------END------------------------
  
  
