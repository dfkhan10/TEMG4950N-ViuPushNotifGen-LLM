from datetime import datetime, timedelta

Holidays = {'1 Jan': 'New Year’s Day', '14 Jan': 'YDPB Negeri Sembilan’s Birthday', 
            '15 Jan': 'YDPB Negeri Sembilan’s Birthday Holiday', '25 Jan': 'Thaipusam', 
            '1 Feb': 'Federal Territory Day', '8 Feb': 'Israk Mikraj', '10-12 Feb': 'Chinese New Year', 
            '20 Feb': 'Independence Declaration Day', '4 Mar': 'Installation of Sultan Terengganu', 
            '12 Mar': 'Awal Ramadan', '23 Mar': 'Sultan of Johor’s Birthday', '28 Mar': 'Nuzul Al-Quran', 
            '29 Mar': 'Good Friday', '10-11 Apr': 'Hari Raya Aidilfitri', '26 Apr': 'Sultan of Terengganu’s Birthday', 
            '1 May': 'Labour Day', '17 May': 'Raja Perlis Birthday', 
            '22 May': 'Wesak Day', '22-23 May': 'Hari Hol Pahang', '30-31 May': 'Harvest Festival', 
            '1-2 Jun': 'Hari Gawai', '3 Jun': 'Agong’s Birthday', '4 Jun': 'Hari Gawai Holiday', 
            '16 Jun': 'Arafat Day', '17 Jun': 'Hari Raya Haji', '18 Jun': 'Hari Raya Haji Holiday', 
            '30 Jun': 'Sultan of Kedah’s Birthday', '7 - 8 Jul': 'Awal Muharram', 
            '9 Jul': 'Georgetown World Heritage City Day', '13 Jul': 'Penang Governor’s Birthday', 
            '22 Jul': 'Sarawak Day', '30 Jul': 'Sultan of Pahang’s Birthday', 
            '11 Aug': 'Hari Hol Almarhum Sultan Iskandar', '24 Aug': 'Melaka Governor’s Birthday', 
            '31 Aug': 'Merdeka Day', '16 Sep': 'Prophet Muhammad’s Birthday', '17 Sep': 'Malaysia Day Holiday', 
            '29 Sep': 'Sultan of Kelantan’s Birthday', '30 Sep': 'Sultan of Kelantan’s Birthday Holiday', 
            '5 Oct': 'Sabah Governor’s Birthday', '12 Oct': 'Sarawak Governor’s Birthday', '31 Oct': 'Deepavali', 
            '1 Nov': 'Sultan of Perak’s Birthday', '13 Nov': 'testing', '15 - 16 Nov': 'testing2', 
            '11 Dec': 'Sultan of Selangor’s Birthday', 
            '24 Dec': 'Christmas Eve', '25 Dec': 'Christmas Day'}


def check_holiday_status(holidays):
    today = datetime.now().strftime('%d %b')
    today_date = datetime.now()
    upcoming_holidays = {}

    print("today: ", today)
    print("today_date: ", today_date)

    for date, holiday_name in holidays.items():

        if '-' in date:
            start_date_str, end_date_str = date.split('-')
            start_date_str = start_date_str + " " + date[-3:]
            print("start_date_str: ", start_date_str)
            print("end_date_str: ", end_date_str)
            start_date = datetime.strptime(start_date_str, '%d %b')
            start_date = start_date.replace(year=datetime.now().year)

            if end_date_str[0] == ' ': #When '7 - 8 Jul', sfter  strip, end_date will become ' 8 Jul', not '8 Jul', which will cause error in end_date = datetime.strptime(end_date_str, '%d %b') if no space in front of '%d %b'
                end_date = datetime.strptime(end_date_str, ' %d %b')
            else:
                end_date = datetime.strptime(end_date_str, '%d %b')
            end_date = end_date.replace(year=datetime.now().year)
            print("start_date: ", start_date)
            print("end_date: ", end_date)

            # if start_date <= today <= end_date:
            #     return f"Today is {holiday_name}"

        else: 
            print('data: ', date)
            # print('-' in date)
            # if date == today:
            #     return f"Today is {holiday_name}"
            
            holiday_date = datetime.strptime(date, '%d %b')
            holiday_date = holiday_date.replace(year=datetime.now().year)
            
            days_until_holiday = (holiday_date - today_date).days
            print(days_until_holiday)
            
            if 0 < days_until_holiday <= 7:
                upcoming_holidays[date] = holiday_name

    if upcoming_holidays:
        upcoming_holiday_str = ', '.join([f"{holiday_name} is coming soon" for holiday_name in upcoming_holidays.values()])
        return upcoming_holiday_str

    return "No upcoming holidays within the next 7 days"



check_holiday_status(Holidays)




