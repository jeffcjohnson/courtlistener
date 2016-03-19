import re

SPECIAL_REGEXES = {
    'tennessee/court_opinions': (
        (re.compile('Supreme Court of Errors and Appeals', re.I), 'tenn'),
        (re.compile('Court of Errors and Appeals', re.I), 'tenn'),
    )
}

FOLDER_DICT = {
    'arkansas/attorney_general_opinion'                       : 'arkattygenop',
    'arkansas/workers_compensation_commission'                : 'arkworkcompcom',
    'california/attorney_general_opinion'                     : 'calattygenop',
    'california/supreme_court_opinions'                       : 'cal',
    'california/court_of_appeal_opinions'                     : 'calctapp',
    'colorado/attorney_general_opinion'                       : 'coloattygenop',
    'colorado/industrial_claim_appeals_office'                : 'coloworkcompcom',
    'connecticut/appellate_court_opinions'                    : 'connappct',
    'connecticut/superior_court_opinions'                     : 'connsuperct',
    'connecticut/workers_compensation_commission'             : 'connworkcompcom',
    'district_of_columbia/court_of_appeals_opinions'          : 'dc',
    'florida/attorney_general_opinion'                        : 'flaattygenop',
    'georgia/supreme_court_opinions'                          : 'ga',
    'georgia/court_of_appeals_opinions'                       : 'gactapp',
    'illinois/appellate_court_opinions'                       : 'illappct',
    'illinois/supreme_court_opinions'                         : 'ill',
    'kansas/attorney_general_opinion'                         : 'kanattygenop',
    'louisiana/attorney_general_opinion'                      : 'laattygenop',
    'maine/supreme_judicial_court_opinions'                   : 'me',
    'maryland/attorney_general_opinion'                       : 'mdattygenop',
    'maryland/court_of_appeals_opinions'                      : 'md',
    'maryland/court_of_special_appeals_opinions'              : 'mdctspecapp',
    #'massachusetts/appellate_court_opinions'                 : 'massappct', -- contains supreme judicial court opinions
    'massachusetts/superior_court_opinions'                   : 'masssuperct',
    'massachusetts/department_of_industrial_accidents'        : 'massworkcompcom',
    'massachusetts/district_court_appellate_division_opinions': 'massdistct',
    'michigan/supreme_court_opinions'                         : 'mich',
    'michigan/court_of_appeals_opinions'                      : 'michctapp',
    'montana/attorney_general_opinion'                        : 'montattygenop',
    'nebraska/attorney_general_opinion'                       : 'nebattygenop',
    'nevada/supreme_court_opinions'                           : 'nev',
    'new_jersey/superior_court_opinions'                      : 'njsuperctappdiv',
    'new_jersey/supreme_court_opinions'                       : 'nj',
    'new_jersey/tax_court_opinions'                           : 'njtaxct',
    'new_york/attorney_general_opinion'                       : 'nyattygenop',
    'new_york/court_of_appeals_opinions'                      : 'ny',
    # This might be part of 'nylowercourts' or might be the only one worth keeping
    'new_york/supreme_court_appellate_division_opinions'      : 'nyappdiv',
    'new_york/miscellaneous_court_opinions'                   : 'nylowercourts',
    'north_carolina/business_court_opinions'                  : 'ncsuperct',
    'north_carolina/industrial_commission'                    : 'ncworkcompcom',
    'ohio/appellate_court_opinions'                           : 'ohioappct',
    'ohio/miscellaneous_court_opinions'                       : 'ohiolowercourts',
    'oklahoma/attorney_general_opinion'                       : 'oklaattygenop',
    'oregon/court_of_appeals_opinions'                        : 'orctapp',
    'oregon/tax_court_opinions'                               : 'ortc',
    'pennsylvania/superior_court_opinions'                    : 'pasuperct',
    'pennsylvania/supreme_court_opinions'                     : 'pa',
    'pennsylvania/commonwealth_court_opinions'                : 'pacommwct',
    'rhode_island/superior_court_opinions'                    : 'risuperct',
    'rhode_island/supreme_court_opinions'                     : 'ri',
    'south_dakota/supreme_court_opinions'                     : 'sd',
    'texas/attorney_general_opinion'                          : 'texattygenop',
    'vermont/supreme_court_opinions'                          : 'vt',
    'virginia/supreme_court_opinions'                         : 'va',
    'virginia/court_of_appeals_opinions'                      : 'vactapp',
    'washington/attorney_general_opinion'                     : 'washattygenop',
    'washington/supreme_court_opinions'                       : 'wash',
    'washington/court_of_appeals_opinions'                    : 'washctapp',
    'west_virginia/supreme_court_opinions'                    : 'wva',
    'wisconsin/attorney_general_opinion'                      : 'wisattygenop'
}