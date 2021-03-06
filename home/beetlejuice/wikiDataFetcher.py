# To know the IDs of property, visit : https://www.wikidata.org/wiki/Wikidata:List_of_properties/en


wdf = Runtime.createAndStart("wikiDataFetcher", "WikiDataFetcher")

query = "Adam Sandler"
wdf.setWebSite("enwiki") 

# Display the label
wdf.setLanguage("en")
print "Label from query : " + wdf.getLabel(query)

# Set language to english
wdf.setLanguage("en")

# Display the description 
print "Description EN : " + wdf.getDescription(query)

# Change language to French and display again the description
wdf.setLanguage("fr")
print "Description FR : " + wdf.getDescription(query)

# Display the identification number of the document
print "Identification number : " + wdf.getId(query)

# Display the description from document identification number
wdf.setLanguage("en")
print "Label from ID Q933 : " + wdf.getLabelById("Q933")

# Display the description from document identification number
wdf.setLanguage("en")
print "Description from ID Q933 : " + wdf.getDescriptionById("Q933")

# Display Date or time  (day, month, year, hour, minute, second, after, before
ID = "P569"
print "BirthDate : " + wdf.getTime(query,ID,"day") +"/" + wdf.getTime(query,ID,"month") + "/" + wdf.getTime(query,ID,"year")