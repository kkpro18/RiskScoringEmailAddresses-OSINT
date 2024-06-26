# this script was created using ChatGPT - https://chat.openai.com/g/g-5nnwHLUL6-dataset-creator

import pandas as pd
import random
import string


# Function to generate random email addresses
def generate_email():
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'aol.com', 'university.edu', 'scamdomain.com', 'example.com']
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(7)) + '@' + random.choice(domains)


# Function to simulate data
def simulate_data(num_records):
    data = []
    for _ in range(num_records):
        email = generate_email()
        validity = random.choice([0, 1])
        holder_name_match = random.choice([0, 1])
        domain = email.split('@')[1]
        domain_type = random.choice(['free', 'corporate', 'educational', 'unknown'])
        domain_quality = random.choice(['high', 'medium', 'low'])
        social_media_presence = random.choice([0, 1])
        data_breach_involvement = random.choice([0, 1])
        email_quality_score = random.randint(0, 100)

    # trends
        # validity 1 = good, 0 = bad
        # holder name = 1 = good, 0 = bad
        # domain type:  corporate, educational = good, free = ok, unknown = ok/bad
        # domain quality = high = good score 66-95, medium = 41-65, low = < 40
        # social media presence, 0 = ok if educational/corporate, 1 = ok if free/unknown/corporate/educational
        # data breach involvement, 1 = low score less than 60, 0 = good for 50+
        # email quality = 70 - 100 = good, 55 - 69 = ok, 40 - 54 = not bad, less than 40 = bad avoid

        # create filter for domain quality...




        # decides email quality score
        if validity == 1 and holder_name_match == 1 and data_breach_involvement == 0 and domain_quality in ['high', 'medium']:
            email_quality_score = random.randint(70, 100)
        elif validity and domain_quality and data_breach_involvement:
            email_quality_score = random.randint(55, 69)
        elif validity and holder_name_match:
            email_quality_score = random.randint(40, 54)
        else:
            email_quality_score = random.randint(0, 40)





        data.append([email, validity, holder_name_match, domain, domain_type, domain_quality,
                     social_media_presence, data_breach_involvement, email_quality_score])

    return data

num_records = 100000
data = simulate_data(num_records)

columns = ['Email Address', 'Validity', 'Holder Name Match', 'Domain', 'Domain Type', 'Domain Quality',
           'Social Media Presence', 'Data Breach Involvement', 'Email Quality Score']
df = pd.DataFrame(data, columns=columns)

df.to_csv('risk_scoring_email_addresses_clean.csv', index=False)




