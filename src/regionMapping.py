import pandas as pd

# Mapping of countries to regions
country_to_region = {
    "Afghanistan": "Asia-Pacific",
    "Albania": "Europe",
    "Algeria": "Middle East/North Africa",
    "Andorra": "Europe",
    "Angola": "Sub-Saharan Africa",
    "Antigua and Barbuda": "Americas",
    "Argentina": "Americas",
    "Armenia": "Europe",
    "Australia": "Asia-Pacific",
    "Austria": "Europe",
    "Azerbaijan": "Europe",
    "Bahamas": "Americas",
    "Bahrain": "Middle East/North Africa",
    "Bangladesh": "Asia-Pacific",
    "Barbados": "Americas",
    "Belarus": "Europe",
    "Belgium": "Europe",
    "Belize": "Americas",
    "Benin": "Sub-Saharan Africa",
    "Bhutan": "Asia-Pacific",
    "Bolivia": "Americas",
    "Bosnia and Herzegovina": "Europe",
    "Botswana": "Sub-Saharan Africa",
    "Brazil": "Americas",
    "Brunei": "Asia-Pacific",
    "Bulgaria": "Europe",
    "Burkina Faso": "Sub-Saharan Africa",
    "Burundi": "Sub-Saharan Africa",
    "Cabo Verde": "Sub-Saharan Africa",
    "Cambodia": "Asia-Pacific",
    "Cameroon": "Sub-Saharan Africa",
    "Canada": "Americas",
    "Central African Republic": "Sub-Saharan Africa",
    "Chad": "Sub-Saharan Africa",
    "Chile": "Americas",
    "China": "Asia-Pacific",
    "Colombia": "Americas",
    "Comoros": "Sub-Saharan Africa",
    "Congo, Democratic Republic of the": "Sub-Saharan Africa",
    "Congo, Republic of the": "Sub-Saharan Africa",
    "Costa Rica": "Americas",
    "Croatia": "Europe",
    "Cuba": "Americas",
    "Cyprus": "Middle East/North Africa",
    "Czech Republic": "Europe",
    "Denmark": "Europe",
    "Djibouti": "Middle East/North Africa",
    "Dominica": "Americas",
    "Dominican Republic": "Americas",
    "Ecuador": "Americas",
    "Egypt": "Middle East/North Africa",
    "El Salvador": "Americas",
    "Equatorial Guinea": "Sub-Saharan Africa",
    "Eritrea": "Sub-Saharan Africa",
    "Estonia": "Europe",
    "Eswatini": "Sub-Saharan Africa",
    "Ethiopia": "Sub-Saharan Africa",
    "Fiji": "Asia-Pacific",
    "Finland": "Europe",
    "France": "Europe",
    "Gabon": "Sub-Saharan Africa",
    "Gambia": "Sub-Saharan Africa",
    "Georgia": "Europe",
    "Germany": "Europe",
    "Ghana": "Sub-Saharan Africa",
    "Greece": "Europe",
    "Grenada": "Americas",
    "Guatemala": "Americas",
    "Guinea": "Sub-Saharan Africa",
    "Guinea-Bissau": "Sub-Saharan Africa",
    "Guyana": "Americas",
    "Haiti": "Americas",
    "Honduras": "Americas",
    "Hungary": "Europe",
    "Iceland": "Europe",
    "India": "Asia-Pacific",
    "Indonesia": "Asia-Pacific",
    "Iran": "Middle East/North Africa",
    "Iraq": "Middle East/North Africa",
    "Ireland": "Europe",
    "Israel": "Middle East/North Africa",
    "Italy": "Europe",
    "Jamaica": "Americas",
    "Japan": "Asia-Pacific",
    "Jordan": "Middle East/North Africa",
    "Kazakhstan": "Asia-Pacific",
    "Kenya": "Sub-Saharan Africa",
    "Kiribati": "Asia-Pacific",
    "Korea, North": "Asia-Pacific",
    "Korea, South": "Asia-Pacific",
    "Kosovo": "Europe",
    "Kuwait": "Middle East/North Africa",
    "Kyrgyzstan": "Asia-Pacific",
    "Laos": "Asia-Pacific",
    "Latvia": "Europe",
    "Lebanon": "Middle East/North Africa",
    "Lesotho": "Sub-Saharan Africa",
    "Liberia": "Sub-Saharan Africa",
    "Libya": "Middle East/North Africa",
    "Liechtenstein": "Europe",
    "Lithuania": "Europe",
    "Luxembourg": "Europe",
    "Madagascar": "Sub-Saharan Africa",
    "Malawi": "Sub-Saharan Africa",
    "Malaysia": "Asia-Pacific",
    "Maldives": "Asia-Pacific",
    "Mali": "Sub-Saharan Africa",
    "Malta": "Europe",
    "Marshall Islands": "Asia-Pacific",
    "Mauritania": "Sub-Saharan Africa",
    "Mauritius": "Sub-Saharan Africa",
    "Mexico": "Americas",
    "Micronesia": "Asia-Pacific",
    "Moldova": "Europe",
    "Monaco": "Europe",
    "Mongolia": "Asia-Pacific",
    "Montenegro": "Europe",
    "Morocco": "Middle East/North Africa",
    "Mozambique": "Sub-Saharan Africa",
    "Myanmar": "Asia-Pacific",
    "Namibia": "Sub-Saharan Africa",
    "Nauru": "Asia-Pacific",
    "Nepal": "Asia-Pacific",
    "Netherlands": "Europe",
    "New Zealand": "Asia-Pacific",
    "Nicaragua": "Americas",
    "Niger": "Sub-Saharan Africa",
    "Nigeria": "Sub-Saharan Africa",
    "North Macedonia": "Europe",
    "Norway": "Europe",
    "Oman": "Middle East/North Africa",
    "Pakistan": "Asia-Pacific",
    "Palau": "Asia-Pacific",
    "Palestine": "Middle East/North Africa",
    "Panama": "Americas",
    "Papua New Guinea": "Asia-Pacific",
    "Paraguay": "Americas",
    "Peru": "Americas",
    "Philippines": "Asia-Pacific",
    "Poland": "Europe",
    "Portugal": "Europe",
    "Qatar": "Middle East/North Africa",
    "Romania": "Europe",
    "Russia": "Europe",
    "Rwanda": "Sub-Saharan Africa",
    "Saint Kitts and Nevis": "Americas",
    "Saint Lucia": "Americas",
    "Saint Vincent and the Grenadines": "Americas",
    "Samoa": "Asia-Pacific",
    "San Marino": "Europe",
    "Sao Tome and Principe": "Sub-Saharan Africa",
    "Saudi Arabia": "Middle East/North Africa",
    "Senegal": "Sub-Saharan Africa",
    "Serbia": "Europe",
    "Seychelles": "Sub-Saharan Africa",
    "Sierra Leone": "Sub-Saharan Africa",
    "Singapore": "Asia-Pacific",
    "Slovakia": "Europe",
    "Slovenia": "Europe",
    "Solomon Islands": "Asia-Pacific",
    "Somalia": "Sub-Saharan Africa",
    "South Africa": "Sub-Saharan Africa",
    "South Sudan": "Sub-Saharan Africa",
    "Spain": "Europe",
    "Sri Lanka": "Asia-Pacific",
    "Sudan": "Sub-Saharan Africa",
    "Suriname": "Americas",
    "Sweden": "Europe",
    "Switzerland": "Europe",
    "Syria": "Middle East/North Africa",
    "Taiwan": "Asia-Pacific",
    "Tajikistan": "Asia-Pacific",
    "Tanzania": "Sub-Saharan Africa",
    "Thailand": "Asia-Pacific",
    "Timor-Leste": "Asia-Pacific",
    "Togo": "Sub-Saharan Africa",
    "Tonga": "Asia-Pacific",
    "Trinidad and Tobago": "Americas",
    "Tunisia": "Middle East/North Africa",
    "Turkey": "Europe",
    "Turkmenistan": "Asia-Pacific",
    "Tuvalu": "Asia-Pacific",
    "Uganda": "Sub-Saharan Africa",
    "Ukraine": "Europe",
    "United Arab Emirates": "Middle East/North Africa",
    "United Kingdom": "Europe",
    "United States": "Americas",
    "Uruguay": "Americas",
    "Uzbekistan": "Asia-Pacific",
    "Vanuatu": "Asia-Pacific",
    "Vatican City": "Europe",
    "Venezuela": "Americas",
    "Vietnam": "Asia-Pacific",
    "Yemen": "Middle East/North Africa",
    "Zambia": "Sub-Saharan Africa",
    "Zimbabwe": "Sub-Saharan Africa"
}



# Read the CSV file
df = pd.read_csv("merged.csv")

# Add a new column "region" based on the mapping
df["region"] = df["Country"].map(country_to_region)

# Save the modified DataFrame back to the CSV file
df.to_csv("merged_with_region.csv", index=False)