#This code contains conversions for different text formats into words

#CONVERTING FROM ROMAN TO INT 
  def romanToInt(s):
      """
     
      :type s: str
      :rtype: int
      """
      
      roman = {'I':1,'II':2,'III':3,'VI':6,'VII':7,'VIII':8,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      
      i = 0
      num = ""
      
      for i in roman:
        if(s==i):
          
          s=roman[i]
          
          
          return (num2words.num2words(s))
  #CONVERTING FRACTION TO WORDS  
  def fraction(s):
    fraction=s.split("/")
    if(fraction[1]=='4'):
      return(num2words.num2words(int(fraction[0])) + " "+ "quarters")
    if(fraction[1]=='2' and fraction[0]=='1'):
      return("and a half")  
    return(num2words.num2words(int(fraction[0])) + " "+ num2words.num2words(int(fraction[1]) , to='ordinal')+"s")

  #CONVERTING UNITS TO WORDS
  def measuring_unit(s):
      """
      :type s: str
      :rtype: int
      """
      print(s)
      m_unit={'cr':'crore','nm':'nanometers','dm':'decimeters','dam':'dekameters','hm':'hectameteres','mi':'miles','m':'meters','cm':'centimeters','km':'kilometers','mm':'millimeters','ha':'hectares','m2':'square meters','cm2':'square centimeters','km2':'square kilometers','kmtwo':'square kilometers','mm2':'square millimeters','ha2':'square hectares','/km':'per kilometers','/cm':'per centimeteres','/km2':'per square kilometers','/ha':'per hectares','/mi':'per miles','km\u00b2':' square kilometers','/km\\u00b2':'per square kilometers','7/km\\u00b2':'seven per square kilometers'}
      
      for i in m_unit:
        if(s==i):
          s=m_unit[i]
          
           
      return (" "+ s)   
  #CONVERTING CURRENCY TO WORDS BOTH UNICODE AND NORMAL
  def currency(s):
    i=0
    s=s.replace("\\u00a3","£")
    s=s.replace("\\u20ac","€")
   
    if(s[i]=='€'):
      #print(s.replace("€","").replace(",","") + " euros")
      return(s.replace("€","") + " euros")
    elif(s[i]=='$'):
      #print(s.replace("$","").replace(",","") + " dollars")
      return(s.replace("$","") + " dollars")
    else:
      #print(s.replace("£","").replace(",","") + " pounds") 
      return(s.replace("£","") + " pounds") 
   

 


  #CONVERTING MULTI PATTERN NUMBERS
  def multipart(s):
    print(s)
    m=[x for x in s]
    
    t=""
    for i in m:
      if(i=='0'):
         i='o'
      elif(i=='-' or i==" "):
         i='sil'

      else:
        i=num2words.num2words(int(i))
      t=t+" "+i
    return(t)

#CONVERTING YEARS TO WORDS
  def year(s):
    splitat=2
    l,r=s[:splitat],s[splitat:]
    
    if(int(l)==20):
       
       return(num2words.num2words(s).replace("thousand and","thousand").replace("hundred and"," ").replace("-",""))
    
    
    if(int(l)<20 and int(r)<=9):
       
       return(num2words.num2words(l)+" "+ "o" +" "+num2words.num2words(r))
    if(int(l)<20 and int(r)>9):
       return(num2words.num2words(l) + " "+num2words.num2words(r).replace("-"," "))
    
 #CONVERTING DATE TO WORDS   
  def date(s):
    m=s.split(" ") 
    #print(m)
    if(len(m)==3):
      return("the" +" " + num2words.num2words(m[0],to='ordinal')+"  "+ "of" +"  "+ m[1]+ "  " +year(m[2]))
    else:
      return("the" +" " + num2words.num2words(m[0],to='ordinal')+"  "+ "of" +"  "+ m[1])
  def months(s):

    m_unit={'01': 'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
    for i in m_unit:
      if(s==i):
       s=m_unit[i]
    return(s)    

 #CONVERTING SECOND DATE FORMAT TO WORDS
  def date2(s):
   
    m=s.split("-")
    print(m)
    print("the" + " "+ num2words.num2words(int(m[2]), to = 'ordinal')+" "+ "of" +   " "+ months(m[1]) + " " + num2words.num2words(m[0]))
    return("the" + " "+ num2words.num2words(int(m[2]), to = 'ordinal')+" "+ "of" +   " "+ months(m[1]) + " " + num2words.num2words(m[0]))
  
  #CONVERTING DECIMAL TO WORDS
  def decimal(s):
   m=s.split(".")
   t=" "
   for x in m[1]:
     t+=num2words.num2words(int(x)) + " "
   #print(t)
   #print(num2words.num2words(int(m[0]))+" "+ "point" +" "+num2words.num2words(int(m[1])))
   return(num2words.num2words(int(m[0])).replace("-"," ")+" "+ "point" +" "+ t)
 
 #CONVERT BYTES TO WORDS
  def convert(s):
     
    
     
     m_byte={'MB':"megabytes",'PB':"petabytes",'GB':"gigabytes",'KB':"kilobytes",' KB':"kilobytes",'AM': 'a m','PM':'p m',' MB':"megabytes",' PB':"petabytes"}
     for i in m_byte:
       if(s==i):
         r=m_byte[i]
     
     return(" "+ r)
 #AVOIDING CACHING OF REGULAR EXPRESSIONS 
  re.purge()
 
 #CONVERTING SID AND INPUT_TOKENS  
  def reconvert(s):
     
     m= s.split(": ")
     #print(":"+" "+str(w2n.word_to_num(m[1])))
     return(":"+" "+ str(w2n.word_to_num(m[1])))

 #CONVERTING TO SELF
  def self(s):
    #print(s)
    if(s=="sid"):
      return("sid")
    if(s=="output_tokens"):
      return("output_tokens")
    if(s=="input_tokens"):
      return("input_tokens")
    if(len(s)==2):
      if(s=='mi'or s=='mm' or s=='km' or s=='cm'or s=='th' or s=='\\u'):
        return(s)
    
    if(s=='January'or s=='February' or s=='March' or s=='April' or s=='May' or s=='June' or s=='July' or s=='August' or s=='September' or s=='October' or s=='November' or s=='December' ):    
      return(s.lower())
    if(s=='million' or s=='Million' or s=='cr' or s=='Rs' or s=='percent'):
      return(s)
   
  
    else:
      return("<self>")
   
  #CONVERT TIME TO WORDS 
  def time(s):
    m=s.split(":")
    if(len(m)==3):
      return(m[0]+" "+"hours"+" "+m[1]+" "+ "minutes"+" "+m[2]+" "+"seconds")
    print(m)
    if(m[1]=='zero'):
      return(m[0])
    else:  
      return(m[0]+ " " + m[1])  

  def complicated_conversion(s):
    m=s.split(" ")
    print(m[0]+" "+num2words.num2words(int(m[1].replace(","," ")), to='ordinal'))
    return(m[0]+" "+num2words.num2words(int(m[1].replace(","," ")), to='ordinal').replace("-"," "))


    
  input_data1 = re.sub(r"\b[a-zA-z][a-z]+[/s_\b]*[a-zA-Z]*", lambda x: self(x.group(0)), input_data1)
  input_data1 = re.sub(r"\b(?=\b[MCDXLVI]{1,6}\b)M{0,4}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})\b", lambda x: romanToInt(x.group(0)) , input_data1)
  #print(input_data1)

 
  
  input_data1 = re.sub(r"\s*[A-Z]B\b",lambda x: convert(x.group(0)), input_data1)
  


  input_data1 = re.sub(r"(\b[A-Z][A-Z]*\b)",lambda x: x.group(0).lower().replace("", " ")[1: -1], input_data1)
  input_data1 = re.sub(r"(\b[A-Z]{3}[a-z]+\b)",lambda x: x.group(0).lower().replace("", " ")[1: -1], input_data1)
  input_data1 = re.sub(r"(\b[A-Z].\b)",lambda x: x.group(0).lower().replace(".", " ")[1: -1], input_data1)
  input_data1 = re.sub(r"([A-Z].\s[A-Z].)",lambda x: x.group(0).lower().replace(".", " ")[1: -1], input_data1)
  input_data1 = re.sub(r"(\b[A-Z]{2}\b)",lambda x: x.group(0).lower().replace("", " ")[1: -1], input_data1)
  input_data1 = re.sub(r"august","<self>", input_data1)
 

 

 #RULES 
  re.purge()
  input_data1 = re.sub(r"[A-Z]+.\sI.",lambda x: x.group(0).lower().replace("."," ") , input_data1)
  input_data1 = re.sub(r"[0-9]+[/][0-9]+",lambda x: fraction(x.group(0)), input_data1)
  
  input_data1 = re.sub(r"[0-9]+([-][0-9]+){3,4}",lambda x: multipart(x.group(0)) , input_data1)
  input_data1 = re.sub(r"[0-9]+(\s[0-9]+){2,4}",lambda x: multipart(x.group(0)) , input_data1)
  input_data1 = re.sub(r"[0-9]+([-][0-9]+){2,4}\s[0-9]",lambda x: multipart(x.group(0)) , input_data1)
  input_data1 = re.sub(r"\\u2014",'sil', input_data1)
  

  input_data1 = re.sub(r"[0-9]+\s[A-za-z]+\s[0-9]{4}",lambda x: date(x.group(0)), input_data1)
  input_data1 = re.sub(r"[0-9]+\s[A-za-z]{3,8}\b",lambda x: date(x.group(0)), input_data1)
  input_data1 = re.sub(r"[0-9]{4}([-][0-9]+){2}",lambda x: date2(x.group(0)), input_data1)

  input_data1 = re.sub(r"([0-9]+m\b)", lambda x: x.group(0).replace("m"," million"), input_data1)
  input_data1 = re.sub(r"([0-9]+M\b)", lambda x: x.group(0).replace("M"," million"), input_data1)
  input_data1 = re.sub(r"(M.\b)", lambda x: x.group(0).replace("M."," m"), input_data1)
  input_data1 = re.sub(r"(b-\b)", lambda x: x.group(0).replace("b-"," b"), input_data1)
  input_data1 = re.sub(r"\\u00a3[0-9]+,[0-9]*",lambda x: currency(x.group(0)), input_data1)
  input_data1 = re.sub(r"\\u00a3[0-9]+\s[a-z]+",lambda x: currency(x.group(0)), input_data1)
  input_data1 = re.sub(r"\\u00a3[0-9]+.[0-9]+\s[a-z]+",lambda x: currency(x.group(0)), input_data1)
  input_data1 = re.sub(r"\\u20ac[0-9]+,[0-9]*",lambda x: currency(x.group(0)), input_data1)
  input_data1 = re.sub(r"\\u20ac[0-9]+\s[a-z]+",lambda x: currency(x.group(0)), input_data1)
  input_data1 = re.sub(r"\\u20ac[0-9]+.[0-9]+\s[a-z]+",lambda x: currency(x.group(0)), input_data1)
  input_data1 = re.sub(r"\b[12][0-9]{3}\b",lambda x: year(x.group(0)), input_data1)
  input_data1 = re.sub(r"[$£€][0-9]{1}[,][0-9]{3}[,][0-9]{3}\b",lambda x: currency(x.group(0).replace(",","")), input_data1)
  input_data1 = re.sub(r"[$£€][0-9]+,[0-9]+",lambda x: currency(x.group(0)), input_data1)
  input_data1 = re.sub(r"[$£€][0-9]+\s[a-z]+",lambda x: currency(x.group(0)), input_data1)
  input_data1 = re.sub(r"[$£€][0-9]+(million)",lambda x: currency(x.group(0)), input_data1)
  input_data1 = re.sub(r"[$£€][0-9]+.[0-9]+\s[a-z]+",lambda x: currency(x.group(0)), input_data1)
  
  
  input_data1 = re.sub(r"([0-9]+[.][0-9]+)", lambda x:decimal(x.group(0)), input_data1)
  input_data1 = re.sub(r"[0-9]*/[a-z0-9]+\\u00b2", lambda x: measuring_unit(x.group(0)), input_data1)
  input_data1 = re.sub(r"[-+]?[0-9]*\.?[0-9]*[a-z0-9]+\\u00b2", lambda x: measuring_unit(x.group(0)), input_data1)
  
  input_data1 = re.sub(r"[a-z]+\\u00b2", lambda x: measuring_unit(x.group(0)), input_data1)

  input_data1 = re.sub(r"/[a-z0-9]+", lambda x: measuring_unit(x.group(0)), input_data1)

  input_data1 = re.sub(r"[-+]?[0-9]*\.?[0-9]*/[a-z0-9]+(two)*", lambda x: measuring_unit(x.group(0)), input_data1)
  #print("HELLO")
  input_data1 = re.sub(r"[a-z]+-[a-z]+", lambda x: x.group(0).replace("-"," "), input_data1)
  input_data1 = re.sub(r"\s[a-zA-Z]{2}\b", lambda x: measuring_unit(x.group(0).strip()), input_data1)
  
  #print(input_data1)
  input_data1 = re.sub(r"Rs","Rupees", input_data1)
  input_data1 = re.sub(r"\brs\b","rupees", input_data1)
  input_data1 = re.sub(r"\sha\b","hectares", input_data1)
  input_data1 = re.sub(r"\'\s"," ", input_data1)
  
  input_data1 = re.sub(r"([0-9]+,[0-9]+)", lambda x: num2words.num2words(int(x.group(0).replace(",",""))).replace("-"," ").replace("thousand and","thousand").replace("hundred and","hundred"), input_data1)
  input_data1 = re.sub(r"[a-z]+\s(\d+),", lambda x: complicated_conversion(x.group(0)), input_data1)
  
  input_data1 = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0))).replace("-"," "), input_data1)
  
  
  #print(input_data1)
  input_data1 = re.sub(r"[a-z]+:\s*[a-z]+\s*[a-z]+", lambda x: time(x.group(0)), input_data1)
  input_data1 = re.sub(r"[a-z]+:\s*[a-z]+:\s*[a-z]+", lambda x: time(x.group(0)), input_data1)
  #print(input_data1)
  input_data1 = re.sub(r"-twenty two", lambda x: x.group(0).replace("-","minus "), input_data1)
  input_data1 = re.sub(r"pm",lambda x: x.group(0).replace("pm"," p m "), input_data1)
  input_data1 = re.sub(r"p.m.",lambda x: x.group(0).replace("p.m."," p m "), input_data1)
  input_data1 = re.sub(r"a.m.",lambda x: x.group(0).replace("a.m."," a m "), input_data1)
  input_data1 = re.sub(r"am",lambda x: x.group(0).replace("am"," a m "), input_data1)
  input_data1 = re.sub(r"pst",lambda x: x.group(0).replace("pst"," p s t "), input_data1)
  input_data1 = re.sub(r"PM",lambda x: x.group(0).replace("PM"," p m "), input_data1)
  input_data1 = re.sub(r"input_tokens",lambda x: x.group(0).replace("input_tokens","output_tokens"), input_data1)
 # input_data1 = re.sub(r"([\b.\b])", " sil ", input_data1)
  input_data1 = re.sub(r":(\s[a-z]+)+-*[a-z]*", lambda x: reconvert(x.group(0)), input_data1)
  input_data1 = re.sub(r"[0-9]+(st)", lambda x: num2words.num2words(int(x.group(0).replace("st","")), to='ordinal'), input_data1)
  input_data1 = re.sub(r"[0-9]+(nd)", lambda x: num2words.num2words(int(x.group(0).replace("nd","")), to='ordinal'), input_data1)
  input_data1 = re.sub(r"[0-9]+(th)", lambda x: num2words.num2words(int(x.group(0).replace("th","")), to='ordinal'), input_data1)

  input_data1 = re.sub(r"[?!.;'()\\//]",  'sil' , input_data1)
 
  input_data1 = re.sub(r"%", " percent ", input_data1)
  input_data1 = re.sub(r"pc", " percent ", input_data1)
 
  input_data1 = re.sub(r"\s\",\",", "\" sil\" , " , input_data1)
  input_data1 = re.sub(r"\s\":\","," \"sil \"," , input_data1)
  input_data1 = re.sub(r" \\", "sil" , input_data1)
  #input_data1 = re.sub(r" \" ", "sil" , input_data1)
  #input_data1 = re.sub(r" ["]["] " , " ["]  ", input_data1)
  input_data1 = re.sub(r"\ba\b","<self>" , input_data1)
  input_data1 = re.sub(r"<self>'<self>","<self>" , input_data1)
  input_data1 = re.sub(r"<self>sils","<self>" , input_data1)
  
  print(input_data1)

  with open("solution_file.json", "w") as outfile:
    outfile.write(input_data1)
