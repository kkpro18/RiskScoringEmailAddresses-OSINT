# this script was created using ChatGPT - https://chat.openai.com/g/g-5nnwHLUL6-dataset-creator


import pandas as pd
import random
import string


def generate_email():
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'aol.com', 'university.edu', 'scamdomain.com', 'example.com']
    letters = string.ascii_lowercase
    name_length = random.randint(5, 10)
    return ''.join(random.choice(letters) for i in range(name_length)) + '@' + random.choice(domains)


def simulate_raw_data(num_records):
    data = []
    for _ in range(num_records):
        email = generate_email()

        # Simulate data collection with variations and missing values
        validity = random.choice([1, 0, None])
        holder_name_match = random.choice([1, 0, None])
        domain = email.split('@')[1]
        domain_type = random.choice(['free', 'corporate', 'educational', 'unknown', None])
        domain_quality = random.choice(['high', 'medium', 'low', None])
        social_media_presence = random.choice([1, 0, None])
        data_breach_involvement = random.choice([1, 0, None])
        blacklist_status = random.choice([1, 0, None])
        email_quality_score = random.choice([random.randint(0, 100), None])

        data.append([email, validity, holder_name_match, domain, domain_type, domain_quality,
                     social_media_presence, data_breach_involvement, blacklist_status, email_quality_score])

    return data


num_records = 100000
data = simulate_raw_data(num_records)

columns = ['Email Address', 'Validity', 'Holder Name Match', 'Domain', 'Domain Type', 'Domain Quality',
           'Social Media Presence', 'Data Breach Involvement', 'Blacklist Status', 'Email Quality Score']
df = pd.DataFrame(data, columns=columns)

df.to_csv('raw_risk_scoring_email_addresses_raw.csv', index=False)
