from APIDump import APIDump

if __name__ == '__main__':
    SITE = APIDump.config_api(100, 250)
    posts = APIDump.get_questions(SITE)
    APIDump.export_json_to_file(posts)