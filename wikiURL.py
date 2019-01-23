def wikiURL(userinput):
    userinput = userinput.strip()
    userinput = userinput.title()
    userinput = userinput.replace(' ','_')
    
    search_url = 'https://en.wikipedia.org/wiki/' + userinput

    return search_url



def fighterName(userinput):
    userinput = userinput.strip()
    userinput = userinput.title()

    return userinput