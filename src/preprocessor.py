import pandas as pd
import numpy as np
import time
import warnings
import os
import requests

class DUMMY_PI:



                                                  #DATA REVEIW AI CHECK
                                                  #INIT PART




  def __init__(self , input = None):

    if input is None:
      input = pd.DataFrame()
    if isinstance(input, (str, os.PathLike)):
      self.input = pd.read_csv(input)

    elif isinstance(input, pd.DataFrame):
        self.input = input.copy()

    else:
        raise TypeError("Input must be a file path or pandas DataFrame.")

    # Initialize prep_data here so it is always available
    self.prep_data = self.input.copy()

  # Ai checking Part

# AI checking Part
  def ai_check(self):

    url = "https://dummy-preprocessor.onrender.com/ai-check"

    try:
        statistics = self.input.describe().to_string()

        response = requests.post(
            url,
            json={"statistics": statistics},
            timeout=120
        )
        if response.status_code == 200:
          result = response.json().get("result")
          if result:
            return result
          print("AI CHECK: Server returned an empty response.")
          return None


        print(f"AI CHECK: Server returned status {response.status_code}.")
        return None

    except requests.exceptions.Timeout:
        print("AI CHECK: Request timed out. Continuing without AI.")
        return None

    except requests.exceptions.ConnectionError:
        print("AI CHECK: No internet connection or server unavailable. Continuing without AI.")
        return None

    except requests.exceptions.RequestException as e:
        print(f"AI CHECK: Network problem: {e}. Continuing without AI.")
        return None

    except (ValueError, KeyError) as e:
        print(f"AI CHECK: Invalid server response: {e}. Continuing without AI.")
        return None



  def get_instruction(self ):

    text_me = """                        \033[92m╔══════════════════════════════════════════════════════════════════════╗
                        ║                                                                      ║
                        ║                                                                      ║
                        ║          ██████╗ ██╗   ██╗███╗   ███╗███╗   ███╗██╗   ██╗            ║
                        ║          ██╔══██╗██║   ██║████╗ ████║████╗ ████║╚██╗ ██╔╝            ║
                        ║          ██║  ██║██║   ██║██╔████╔██║██╔████╔██║ ╚████╔╝             ║
                        ║          ██║  ██║██║   ██║██║╚██╔╝██║██║╚██╔╝██║  ╚██╔╝              ║
                        ║          ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║ ╚═╝ ██║   ██║               ║
                        ║          ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝   ╚═╝               ║
                        ║                                                                      ║
                        ║                 D U M M Y   P R E P R O C E S S O R                  ║
                        ║                                                                      ║
                        ║                                                                      ║
                        ╚══════════════════════════════════════════════════════════════════════╝\033[0m"""

    for el in text_me:
      print(el , end="")
      time.sleep(0.001)

    print()
    instruction = '''
    INSTRUCTION !!!



                        ------  A U T O  F I X  ____ Preprocessing Data ------



    -- x = DUMMY_PI(input = "YOUR DATA PATH OR pd.DataFrame")
              \033[92mInit process\033[0m

    ````Method name: \033[91mx.get_auto_fix()\033[0m

              Short info : get_auto_fix()
              |||  Automatically handles preprocessing tasks:
              <Review Data> <Missing Data Handling> <Time Column Handling>
              <Normalisation> <Encoding (when enabled)> |||

              Param Def
              \033[93mDefault\033[0m ___ \033[92minteractive=False\033[0m ___ if True --> (you get manual access to choose mean or median values, or stop the process)

              \033[93mDefault\033[0m ___ \033[92mnormalisation=False\033[0m ___ if True --> (numerical values will be normalised)

              \033[93mDefault\033[0m ___ \033[92mtrain=True\033[0m ___ (if train=True, we save min and max values from training data. If train=False, we reuse the saved min and max values from training data)

              \033[93mDefault\033[0m ___ \033[92mencoding=False\033[0m ___ if True --> (categorical values will be one-hot encoded)



                          ------ M A N U A L  F I X ____ Preprocessing Data ------



    -- x = DUMMY_PI(input = "YOUR DATA PATH OR pd.DataFrame")
              \033[92mInit process\033[0m

    ````Method name : \033[91mx.get_view()\033[0m:

              Short info : get_view()
              ||| AI Review (\033[91mInternet connection required\033[0m)
              <Detecting Missing Data> <Detecting Time Columns> <Data Overview> |||

              Param Def
              \033[93mDefault\033[0m ___ \033[92mai_review=True\033[0m ___ if False --> (ai_check() method will not be activated)

              \033[93mDefault\033[0m ___ \033[92mdescribe=True\033[0m ___ if False --> (pd.describe() will not be printed)



    ````Method name : \033[91mx.get_data_extract()\033[0m

              Short info : get_data_extract()
              ||| <Unix Timestamp Detection --> Datetime>
              <Converting Datetime into Trainable Features> |||

              Param Def
              \033[93mDefault\033[0m ___ #\033[92mdate_extract = Dictionary --> {All Params:None}\033[0m

                          date_extract = {"year":None , "month":None, "day_of_week":None,
                                          "day_of_month":None, "week_of_year":None,
                                          "day_of_year":None, "hour_of_week":None,
                                          "second":None, "minute":None,
                                          "millisecond":None, "hour":None}



    ````Method name : \033[91mx.get_fill_missing()\033[0m

              Short info : get_fill_missing()
              ||| <Filling Missing Numerical and Non-Numerical Data>
              <Automatically Choosing Mean or Median Based on Practical Use>
              <Interquartile Range Calculation to Help Decide Between Mean and Median> |||

              \033[93mDefault\033[0m ___ #\033[92moperations="auto"\033[0m
              if operations="custom" --> (you can fix specific columns by providing columns=[])

              \033[93mDefault\033[0m ___ #\033[92mcolumns=None\033[0m
              if None --> (the method will process all detected missing-value columns)
              \033[91mcolumns = column names should be provided as a list\033[0m

              \033[93mDefault\033[0m ___ #\033[92minter=True\033[0m
              inter means INTERACTION. It activates the response() method,
              allowing users to manually choose mean or median values
              when filling missing data, or stop the process.

              \033[93mDefault\033[0m ___ #\033[92mnorma=False\033[0m
              norma means NORMALISATION. If True, numerical columns will
              be normalised after missing-value handling.



    ````Method name : \033[91mx.normalize()\033[0m

              Short info : normalize()
              ||| <Normalisation> <Saving Min and Max Values> |||

              \033[93mDefault\033[0m ___ #\033[92mtrain=True\033[0m
              --> (if train=True, save min and max values from training data.
              If train=False, reuse the saved min and max values from training data)



    ````Method name : \033[91mx.one_hot_encode()\033[0m

              \033[93mDefault\033[0m ___ #\033[92mexclude=None\033[0m
              --> (you can exclude specific columns)

              \033[93mDefault\033[0m ___ #\033[92mmax_categories=100\033[0m
              --> (specify the maximum number of unique categories per column
              to prevent unnecessary feature expansion)



                      \033[92mWARNING !\033[0m
              High-cardinality columns may be skipped.
              Skipped columns will remain in their original format.



    ````Method name : \033[91mx.normalize_y()\033[0m

              \033[93mParameter\033[0m ___ #\033[92my_true\033[0m
              --> (target values will be normalised separately using their own min and max values)



    ````Method name : \033[91mx.back_norm()\033[0m

              \033[93mParameter\033[0m ___ #\033[92mprediction\033[0m
              --> (converts normalised predictions back to their original scale
              using the saved min and max values from training target data)



    '''
    print("\n\n",instruction)
  def dtype_check(self):
    df = self.input.copy()
    self.check_list = {}
    for col in df.select_dtypes(include=["object", "string" ,"float"]).columns:

        numeric = pd.to_numeric(df[col], errors="coerce")

        valid = df[col].notna()

        if valid.sum() == 0:
            continue

        numeric_rate = numeric.notna().sum() / valid.sum()

        self.check_list[col] = numeric_rate * 100

  # Veiw Data
  def get_veiw(self  ,ai_review = True ,describe = True):

    self.dtype_check()

    if hasattr(self , "prep_data"):
      self.input = self.prep_data


    self.raw_columns = {el[0] : el[1] for el in zip(self.input.columns , self.input.count())}
    median_vol =  np.median(list(self.raw_columns.values()))

    print("\n")
    print(f"\033[92mDataset inspection\n\nRows : {median_vol}\nColunms : {len(self.raw_columns)}\033[0m\n\n")

                                                                                    # We will save missing value coulmn names in self.missing value

    self.missing_value = []
    total_rows = len(self.input)
    obj = []

    for key, val in self.raw_columns.items():
      if self.raw_columns[key] < total_rows:
                                                                                    #Missing value view
        self.missing_value.append(key)
        self.missing_precent = (self.input[key].isna().sum() / len(self.input) * 100)

        print(f"\033[92mMissing value : {key} \033[0m",("_"*(25-len(key))) ,f"  \033[91m{round(self.missing_precent ,2)}%\033[0m")

      if self.input[key].dtype == "object":
                                                                                      #Categorical coulmn view
        obj.append(self.input[key].dtype == "object")
      elif self.input[key].dtype != "object":
        obj.append(self.input[key].dtype == "object")

    for key ,val in self.check_list.items():
      if 0 <  val < 100:
        print(f"WARNING : {key} DATA CONTAIN MIXED TYPE VALUES __ {val}")

    if any(obj):
      print("\033[92mCategorical Column detected  \033[0m" ,"_"*13 ,"  \033[91mD e t e c t e d\033[0m")

    else:
      print("\033[92mCategorical Column detected  \033[0m" ,"_"*13 ,"  \033[92mN O T  D E T E C T E D\033[0m")

                                                                                        #Date coulmns view
    if self.date_check() or self.detect_unix_timestamp():
      print("\033[92mDate Column \033[0m","_"*30,"  \033[91mD e t e c t e d\033[0m")
    if np.mean(self.input.count()) == median_vol:
      print("\033[92mMissing value : \033[0m",("_"*(33-len(key))) ,"  \033[92mN O T  D E T E C T E D\033[0m")
    if ai_review:
        try:
            result = self.ai_check()

            if result:
                print(
                    f"\n\n\033[93mA I   R E V I E W\033[0m : "
                    f"\033[96m{result}\033[0m\n\n"
                )
            else:
                print("\nAI REVIEW: Unavailable. Continuing preprocessing.\n")

        except Exception as e:
            print(f"\nAI REVIEW ERROR: {e}. Continuing preprocessing.\n")
    if describe:
      print(self.input.describe())






                                                      # TIME RELATED DATA





  # Date chcking is it contain date or not date format  -- datetime

  def date_check(self):

    # if hasattr(self , "get_fill_missing"):
    #   self.input = self.prep_data

    date_columns = []

    for col in self.input.columns:

        if not (
            pd.api.types.is_object_dtype(self.input[col])
            or pd.api.types.is_datetime64_any_dtype(self.input[col])
        ):
            continue

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)

            converted = pd.to_datetime(
                self.input[col],
                errors="coerce",
                format="mixed"
            )

        non_missing = self.input[col].notna().sum()

        if non_missing == 0:
            continue

        success_rate = converted.notna().sum() / non_missing

        if success_rate >= 0.8:
            date_columns.append(col)
            # print(f"Date column detected: {col}")

    return date_columns


  # unix date format checking

  def detect_unix_timestamp(self):

    unix_columns = {}

    for col in self.input.columns:

        if not pd.api.types.is_numeric_dtype(self.input[col]):
            continue

        sample = self.input[col].dropna()

        if len(sample) < 3:
            continue

        sample = sample.sample(n=3, random_state=42)

        for unit in ["s", "ms"]:

            converted = pd.to_datetime(
                sample,
                unit=unit,
                errors="coerce",
                utc=True
            )

            # Check whether all 3 values produce plausible dates
            if converted.notna().all():

                years_valid = converted.dt.year.between(
                    2000, 2100
                ).all()

                if years_valid:
                    unix_columns[col] = unit
                    break

    return unix_columns



  # copnverting unix_timestamp to date time :

  def unix_timestamp_converter(self, key):
    unix_cols = self.detect_unix_timestamp()
    if key in unix_cols:
      unit = unix_cols[key]
      self.time_col = pd.to_datetime(self.input[key], unit=unit, errors="coerce")
      return self.time_col
    return None


  # Date components

  def date_components(self , series):

    values = series.dropna().astype(str).head(100)

    result = {
        "has_year": False,
        "has_month": False,
        "has_day": False,
        "has_hour": False,
        "has_minute": False,
        "has_second": False,
        "has_millisecond" : False
    }

    for value in values:

        try:
            parsed = pd.to_datetime(value, format="mixed")

            if parsed.year:
                result["has_year"] = True

            if parsed.month:
                result["has_month"] = True

            if parsed.day:
                result["has_day"] = True
            if ":" in value:

                result["has_hour"] = True

                time_part = value.split()[-1]
                time_parts = time_part.split(":")

                if len(time_parts) >= 2:
                    result["has_minute"] = True

                if len(time_parts) >= 3:
                    result["has_second"] = True

                if len(time_parts) >= 3 and "." in time_parts[2]:
                    result["has_millisecond"] = True

        except (ValueError, TypeError):
            continue

    return result

  # makes dictionary from both date types

  def date_columns_dict(self):

    date_columns = {}

    text_dates = self.date_check()
    unix_dates = self.detect_unix_timestamp()

    self._parsed_date_columns = {}

    # Regular date columns
    for col in text_dates:

        parsed = pd.to_datetime(
            self.input[col],
            errors="coerce",
            format="mixed"
        )

        self._parsed_date_columns[col] = parsed
        date_columns[col] = self.date_components(parsed)

    # Unix timestamp columns
    for col, unit in unix_dates.items():

        parsed = pd.to_datetime(
            self.input[col],
            unit=unit,
            errors="coerce",
            utc=True
        )

        self._parsed_date_columns[col] = parsed
        date_columns[col] = self.date_components(parsed)

    return date_columns



  # Get date

  def get_data_extract(self , date_extract = {"year":None , "month":None,
                                              "day_of_week":None,"day_of_month":None,"week_of_year":None,
                                               "day_of_year":None,"hour_of_week":None,
                                               "second":None ,"minute":None,"millisecond":None, "hour":None}) :
    date_info = self.date_columns_dict()
    self.added_date_value = []
    self.input_x = self.input.copy()

    # date_extract =  {key :True for key  ,val in date_extract.items()}

    for col_n  , val  in date_info.items():
      # for chr_feature , bool_val in val.items():

      self.input_x[col_n] = self._parsed_date_columns[col_n]

      if date_info[col_n]["has_year"] and date_info[col_n]["has_month"] and date_info[col_n]["has_day"]:

        if "month" in date_extract.keys() and date_extract.get("month"): # keys( checks deos this feature exist ) , get() checks true or false
          self.input_x["month"] = self.input_x[col_n].dt.month
          self.added_date_value.append("month")
        if "year" in date_extract.keys() and date_extract.get("year"):
          self.input_x["year"] = self.input_x[col_n].dt.year
          self.added_date_value.append("year")
        if "day_of_week" in date_extract.keys() and date_extract.get("day_of_week"):
          self.input_x["day_of_week"] = self.input_x[col_n].dt.dayofweek
          self.added_date_value.append("day_of_week")
        if "day_of_month" in date_extract.keys() and date_extract.get("day_of_month"):
          self.input_x["day_of_month"] = self.input_x[col_n].dt.day
          self.added_date_value.append("day_of_month")
        if "week_of_year" in date_extract.keys() and date_extract.get("week_of_year"):
          self.input_x["week_of_year"] = self.input_x[col_n].dt.isocalendar().week.astype(int)
          self.added_date_value.append("week_of_year")
        if "day_of_year" in date_extract.keys() and date_extract.get("day_of_year"):
          self.input_x["day_of_year"] = self.input_x[col_n].dt.dayofyear
          self.added_date_value.append("day_of_year")

        if date_info[col_n]["has_hour"] and date_info[col_n]["has_minute"]:
          if "hour_of_week" in date_extract.keys() and date_extract.get("hour_of_week"):
            self.input_x["hour_of_week"] = (
            self.input_x[col_n].dt.dayofweek * 24 + self.input_x[col_n].dt.hour)
            self.added_date_value.append("hour_of_week")
          if "minute" in date_extract.keys() and date_extract.get("minute"):
            self.input_x["minute"] = self.input_x[col_n].dt.minute
            self.added_date_value.append("minute")



      if date_info[col_n]["has_hour"]:
        self.input_x["hour"] = self.input_x[col_n].dt.hour
        self.added_date_value.append("hour")
      if date_info[col_n]["has_minute"]:
        if "minute" in date_extract.keys() and date_extract.get("minute"):
          self.input_x["minute"] = self.input_x[col_n].dt.minute
          self.added_date_value.append("minute")
      if  date_info[col_n]["has_second"]:
        if "second" in date_extract.keys() and date_extract.get("second"):
          self.input_x["second"] = self.input_x[col_n].dt.second
          self.added_date_value.append("has_second")

      if date_info[col_n]["has_millisecond"]:
        if "millisecond" in date_extract.keys() and date_extract.get("millisecond"):
          self.input_x["millisecond"] = self.input_x[col_n].dt.microsecond // 1000
          self.added_date_value.append("millisecond")



      if any(date_extract.values()):
        self.input_x = self.input_x.drop(columns=[col_n])

    self.prep_data = self.input_x
    print(f"\033[92mget_data_extract mathod added\033[0m ___  {self.added_date_value}\n\n")
    return self.input_x





                                                             # MISSING VALUES HANDLING





  # Interquartile range claculation

  def get_iqr(self, column_name):

      values = self.input[column_name].dropna()

      if values.empty:
          return 0

      q1 = values.quantile(0.25)
      q3 = values.quantile(0.75)

      iqr = q3 - q1

      low = q1 - (1.5 * iqr)
      high = q3 + (1.5 * iqr)

      outliers = ((values < low) | (values > high)).sum()

      outlier_percent = (outliers / len(values)) * 100

      return outlier_percent


  # Missing value response checking

  def response(self, val , interactive = True):
      self.method = "mean"
      response_user = None
      self.contin = True
      self.missing_precent = (
        self.input[val].isna().mean() * 100)


      if hasattr(self, "missing_precent"):

        if self.missing_precent < 5:
          self.method = "mean"
          return  # Safely exit early since no user prompt is needed

        if interactive :
          if 5 < self.missing_precent < 30:
            response_user = input(
                f"Missing values {val}__{round((self.missing_precent), 2)}% ______"
                " Do you agree use Median value ? Y/N/STOP ___  "
            )

          elif self.missing_precent >= 30:
            response_user2 = input(
                f"\033[93mWarning !\033[0m  \nMissing values"
                f" {int(self.missing_precent)}%\nAdvice - checking Data ...  \nDo you"
                " agree use Median value ? Y/N/STOP___  "
            )
            if response_user2.upper() == "Y":
              self.method = "median"
              return
            elif response_user2.upper() in ["STOP", "N"]:
              self.contin = False
              return
            else:
              self.contin = False
              return

          # Safe check: only evaluate if user input was captured
          if response_user and response_user.upper() == "Y":
            self.method = "median"
          elif response_user and response_user.upper() == "N":
            if self.get_iqr(column_name=val) > 1:
              response_user_iqr = input(
                  "Interquartile range > 1 --> Effects to mean value  ____ Do you"
                  " want to continue ? __ Y/N/STOP___ "
              )
              if response_user_iqr.upper() == "Y":
                self.method = "mean"
              elif response_user_iqr.upper() == "N":
                self.method = "median"
              elif response_user_iqr.upper() == "STOP":
                print("Operation cancelled.")
                self.contin = False
                return self.input
              else:
                print(f"Given response  __  {response_user_iqr} is not valid Enter ")
                self.contin = False
            else:
              print("Missing value filling mode set to MEAN (not median)")
              self.method = "mean"
          elif response_user and response_user.upper() == "STOP":
            print("Operation cancelled.")
            self.contin = False
            return self.input
          elif response_user:
            print(f"Given response  __  {response_user} is not valid Enter ")
            self.contin = False

        # interactive False
        else :
          if 5 < self.missing_precent < 30:
            self.method = "median"
          elif self.missing_precent >= 30:
            print("Missing data more than 30% ")
            self.contin = False

  #numeric mising values checking

  def numeric_miss_val(self , input_c):

    if self.input[input_c].notna().sum() == 0:
      print(f"{input_c}: No valid values available for filling.")
      return

    if self.method :

      iqr_txt = ""

      if self.get_iqr(column_name = input_c) > 1 and self.method == "median" :
        mean_calc = self.input[input_c].median()
        self.method_txt = "M E D I A N  V A L U E S"
        self.input[input_c] = self.input[input_c].fillna(                          #filling with median volue if numeric
              mean_calc)
        iqr_txt = f"{input_c.upper()}  _________  Interquartile range ((x < low) | (x > high)) outlier_percent = {round(self.get_iqr(column_name = input_c) ,2)} %\n"

      else :
        if self.method == "mean":
          mean_calc = self.input[input_c].mean()
          self.method_txt = "M E A N   V A L U E S"
          self.input[input_c] = self.input[input_c].fillna(                          #filling with mean volue if numeric
              mean_calc)
        else:                                                            # if data contain more than 5% missing data median will be used
          mean_calc = self.input[input_c].median()
          self.method_txt = "M E D I A N  V A L U E S"
          self.input[input_c] = self.input[input_c].fillna(                          #filling with median volue if numeric
              mean_calc)
      print(f"\n\nMissing value : {input_c} ",("_"*(25-len(input_c))) , f"\033[92mF I L L E D   W I T H   {self.method_txt}\033[0m\n{iqr_txt}")



  #non numeric missing val checking

  def non_numeric_mis_val(self, input_c, norm=False):

    date_columns = set(self.date_check())
    unix_columns = set(self.detect_unix_timestamp())

    all_date_columns = date_columns | unix_columns

    if input_c in all_date_columns:
      print(f"{input_c} is a date column. Skipping automatic filling.")
      return

    modes = self.input[input_c].mode()

    if not modes.empty:
      fill_value = modes.iloc[0]

      self.input[input_c] = self.input[input_c].fillna(fill_value)

      print(f"Missing value : {input_c} ",
        "_" * (25 - len(input_c)),
         "\033[92mF I L L E D   W I T H   M O S T   F R E Q U E N T   V A L U E\033[0m")

      if norm:
        self.input[input_c] = self.input[input_c].astype("category").cat.codes

    else:
      print(f"No valid mode found for {input_c}. Skipping.")




  # Main missing value



  def get_fill_missing(self, operations="auto", exclude_columns = None,columns=None, inter=True, norma=False):

    self.exclude_columns(columns=exclude_columns)
    self.norma = norma

    self.get_veiw()
    # No missing values
    if not self.missing_value:

        print("\n\n")
        print(
            "MISSING VALUE : _________________________",
            "\033[92mN O T  D E T E C T E D\033[0m"
        )
        print("\n\n")

        self.prep_data = self.input.copy()
        print(self.prep_data.describe())
        return self.prep_data

    # Select columns
    if operations == "auto":

        list_mis_val = self.missing_value.copy()

    elif operations == "custom":

        if columns:
            if all(x in self.input.columns for x in columns):
                list_mis_val = columns.copy()
            else:
                print("INPUT IS NOT VALID. PLEASE CHECK columns.")
                return

        else:
            print("PLEASE ENTER columns.")
            return

    else:
        print("INPUT FOR operations IS NOT VALID!")
        return

    # Detect date columns once
    date_columns = set(self.date_check())
    unix_columns = set(self.detect_unix_timestamp())

    all_date_columns = date_columns | unix_columns

    self.prep_data = self.input.copy()

    processed_columns = []

    for c in list_mis_val:

        # Skip date columns
        if c in all_date_columns:
            print(f"{c}: Date column detected. Skipping automatic filling.")
            continue

        # Skip columns that have no missing values
        if not self.input[c].isna().any():
            processed_columns.append(c)
            continue

        # Ask user / select filling method
        self.response(c, interactive=inter)

        if not self.contin:
            break

        # Numeric or non-numeric filling
        if pd.api.types.is_numeric_dtype(self.input[c]):

            self.numeric_miss_val(input_c=c)

        else:

            self.non_numeric_mis_val(
                input_c=c,
                norm=norma
            )

        # Update prepared data
        self.prep_data[c] = self.input[c]

        # Track successfully processed columns
        if not self.input[c].isna().any():
            processed_columns.append(c)

    # Preserve columns that still need processing
    self.missing_value = [
        c for c in self.missing_value
        if c not in processed_columns
    ]

    self.restore_columns()
    return self.prep_data


                                        #NORMALISATION PART


  def normalize(self, train=True ,manual = True):

    if manual:
      self.norma = True
    if not hasattr(self, "prep_data") or not self.norma:
        return

    numeric_cols = self.prep_data.select_dtypes(
        include="number"
    ).columns

    if train:

        self.norm_params = {}

        for col in numeric_cols:
            self.norm_params[col] = {
                "min": self.prep_data[col].min(),
                "max": self.prep_data[col].max()
            }

    elif not self.norm_params:
        raise ValueError(
            "No training normalization parameters found. "
            "Fit using training data first."
        )

    for col in numeric_cols:

        if col not in self.norm_params:
            raise ValueError(f"Missing normalization parameters for {col}")

        min_val = self.norm_params[col]["min"]
        max_val = self.norm_params[col]["max"]

        if max_val != min_val:
            self.prep_data[col] = (
                self.prep_data[col] - min_val
            ) / (max_val - min_val)

        else:
            self.prep_data[col] = 0.0

    return self.prep_data

# Y_TRUE NORMOLISATION

  def normalize_y(self, y_true):

    self.y_min = np.min(y_true)
    self.y_max = np.max(y_true)

    if self.y_max == self.y_min:
        raise ValueError("Target values have zero range.")

    return (y_true - self.y_min) / (self.y_max - self.y_min)

  def back_norm(self, prediction):

    if not hasattr(self, "y_min"):
        raise ValueError("Normalize y_true before using back_norm().")

    return prediction * (self.y_max - self.y_min) + self.y_min





  # One hot encoding part


  def one_hot_encode(self, train=True, exclude=None, max_categories=100):

    if not hasattr(self, "prep_data"):
        raise ValueError("Run get_fill_missing() before one_hot_encode().")

    exclude = set(exclude or [])

    # Find date columns so we don't encode them
    date_columns = set(self.date_check())
    unix_columns = set(self.detect_unix_timestamp())

    skip_columns = date_columns | unix_columns | exclude

    # Select categorical columns
    if train:

        categorical_cols = [
            col for col in self.prep_data.columns
            if (
                pd.api.types.is_object_dtype(self.prep_data[col])
                or pd.api.types.is_string_dtype(self.prep_data[col])
                or isinstance(self.prep_data[col].dtype, pd.CategoricalDtype)
            )
            and col not in skip_columns
        ]

        self.onehot_categories = {}
        self.onehot_encoded_columns = {}

        for col in categorical_cols:

            categories = list(pd.unique(self.prep_data[col].dropna()))

            # Avoid creating thousands of features
            if len(categories) > max_categories:
                print(
                    f"{col}: {len(categories)} unique values. "
                    "Skipped due to high cardinality."
                )
                continue

            if not categories:
                print(f"{col}: No valid categories. Skipping.")
                continue

            self.onehot_categories[col] = categories

            encoded = pd.get_dummies(
                pd.Categorical(
                    self.prep_data[col],
                    categories=categories
                ),
                prefix=col,
                dtype="int8"
            )

            self.onehot_encoded_columns[col] = encoded.columns.tolist()

            self.prep_data = pd.concat(
                [self.prep_data.drop(columns=[col]), encoded],
                axis=1
            )

    else:

        if not hasattr(self, "onehot_categories"):
            raise ValueError(
                "No training categories found. Run one_hot_encode(train=True) first."
            )

        for col, categories in self.onehot_categories.items():

            if col not in self.prep_data.columns:
                raise ValueError(
                    f"Column '{col}' is missing from validation data."
                )

            encoded = pd.get_dummies(
                pd.Categorical(
                    self.prep_data[col],
                    categories=categories
                ),
                prefix=col,
                dtype="int8"
            )

            # Guarantee the same columns as training
            encoded = encoded.reindex(
                columns=self.onehot_encoded_columns[col],
                fill_value=0
            )

            self.prep_data = pd.concat(
                [self.prep_data.drop(columns=[col]), encoded],
                axis=1
            )

    print("ONE-HOT ENCODING COMPLETED")
    return self.prep_data
#
  def exclude_columns(self, columns=None):

    if not columns:
        self.except_data = pd.DataFrame(index=self.prep_data.index)
        return

    if not all(col in self.prep_data.columns for col in columns):
        raise ValueError("Some columns do not exist in the dataset.")

    self.except_data = self.prep_data[columns].copy()

    self.prep_data = self.prep_data.drop(columns=columns)


  def restore_columns(self):

    if hasattr(self, "except_data") and not self.except_data.empty:
        self.prep_data = pd.concat(
            [self.prep_data, self.except_data.loc[self.prep_data.index]],
            axis=1
        )

    return self.prep_data

                                              #GET AUTO FIX



  def get_auto_fix(
    self,
    interactive=False,
    exclude_columns=None,
    normalisation=False,
    train=True,
    encoding=False,
    max_categories=100
  ):
    if not hasattr(self , "get_veiw"):
      self.get_veiw(describe=False)

    self.exclude_columns(columns=exclude_columns)

    self.get_fill_missing(
        operations="auto",
        inter=interactive,
        norma=normalisation
    )

    date_extract_val = {
        "year": True,
        "month": True,
        "day_of_week": True,
        "day_of_month": True,
        "week_of_year": True,
        "day_of_year": True,
        "hour_of_week": True,
        "second": True,
        "minute": True,
        "millisecond": True,
        "hour": True
    }

    self.get_data_extract(date_extract=date_extract_val)

    self.normalize(train=train , manual = normalisation)

    if encoding:
        self.one_hot_encode(
            train=train,
            max_categories=max_categories
        )

    self.restore_columns()

    return self.prep_data
