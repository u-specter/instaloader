import instaloader

ig = instaloader.Instaloader()
dp = input("Instagram userni kiriting: ")

ig.download_profile(dp, profile_pic_only=True)