from cparse import main

def test():
    args = main._init_args()
    args.rootpath = r"C:\Users\ADK\Documents\arhams-workspace\extra_projects\dummy_project"
    
    main._run(args)

test()