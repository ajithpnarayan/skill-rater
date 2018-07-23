from skillrater import SkillRater


if __name__ == "__main__":

    s = SkillRater() 

    data = s.get_info('sivasama')
    print(data[0],"\t\t\tLocation:",data[1],"\t\t\tFollowers:",data[2],"\t\t\tFollowing:",data[3])

    pull_requests = s.get_pull_requests('sivasama')

    list_langs = s.list_languages('sivasama', 'accepted-codes')
    print(list_langs)