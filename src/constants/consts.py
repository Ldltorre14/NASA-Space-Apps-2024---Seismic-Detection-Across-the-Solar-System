import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


#  ---    ---        ---       ---------    ----------
#  ----  ----      -------     ---   ---    ----
#  ----------     ---___---    ---------    ----------
#  ---    ---     ---   ---    ---  ---           ---- 
#  ---    ---     ---   ---    ---  -----   ----------        

#   TEST DATA
MARS_TEST_DATA = os.path.join(PROJECT_ROOT, "data", "mars", "test", "data")

#   TRAINING DATA
MARS_TRAINING_CATALOG_DIRECTORY = os.path.join(PROJECT_ROOT, "data", "mars", "training", "catalogs")
MARS_TRAINING_DATA_DIRECTORY = os.path.join(PROJECT_ROOT, "data", "mars", "training", "data") 
MARS_TRAINING_PLOTS_DIRECTORY = os.path.join(PROJECT_ROOT, "data", "mars", "training", "plots")




#   ---    ---      --------        --------     -------   ----
#   ----  ----     ----------      ----------    --------  ----
#   ----------    ---      ---    ---      ---   ----  --- ----
#   ---    ---     ----------      ----------    ----   -------
#   ---    ---      --------        --------     ----    ------

#   TEST DATA
LUNAR_TEST_DATA_S12_GRADE_B = os.path.join(PROJECT_ROOT, "data", "lunar", "test", "data", "S12_GradeB")
LUNAR_TEST_DATA_S15_GRADE_A = os.path.join(PROJECT_ROOT, "data", "lunar", "test", "data", "S15_GradeA")
LUNAR_TEST_DATA_S15_GRADE_B = os.path.join(PROJECT_ROOT, "data", "lunar", "test", "data", "S15_GradeB")
LUNAR_TEST_DATA_S16_GRADE_A = os.path.join(PROJECT_ROOT, "data", "lunar", "test", "data", "S16_GradeA")
LUNAR_TEST_DATA_S16_GRADE_B = os.path.join(PROJECT_ROOT, "data", "lunar", "test", "data", "S16_GradeB")

LUNAR_TEST_DATA_S15_GRADE_B = "./data/lunar/test/data/S15_GradeB"
LUNAR_TEST_DATA_S16_GRADE_A = "./data/lunar/test/data/S16_GradeA"
LUNAR_TEST_DATA_S16_GRADE_B = "./data/lunar/test/data/S16_GradeB"


#   TRAINING DATA
LUNAR_TRAINING_CATALOG_DIRECTORY = os.path.join(PROJECT_ROOT, "data", "lunar", "training", "catalogs")
LUNAR_TRAINING_DATA_DIRECTORY = os.path.join(PROJECT_ROOT, "data", "lunar", "training", "data", "S12_GradeA")
LUNAR_TRAINING_PLOTS_DIRECTORY = os.path.join(PROJECT_ROOT, "data", "lunar", "training", "plots")
