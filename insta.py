import instaloader
import os

def download_reels(username, max_reels):
    # Create an instance of Instaloader
    L = instaloader.Instaloader(download_comments=False, post_metadata_txt_pattern='')

    # Login (optional) for private profiles
    # L.login('your_username', 'your_password')

    # Fetch posts from the given profile
    profile = instaloader.Profile.from_username(L.context, username)

    # Counter to limit the number of reels to download
    reel_count = 0

    # Iterate over all posts in the profile
    for post in profile.get_posts():
        # Download only video posts that are Instagram reels
        if post.is_video and post.typename == 'GraphVideo':  # Reels are video posts
            print(f"Downloading reel from {post.date}")
            try:
                L.download_post(post, target=f"{username}_reels")
                reel_count += 1
            except Exception as e:
                print(f"Error downloading reel: {e}")

            # Stop after downloading the specified number of reels
            if reel_count >= max_reels:
                print(f"Downloaded {reel_count} reels.")
                break

            # Remove associated non-video files (like .jpg, .json, .json.xz)
            reel_directory = f"{username}_reels"
            for filename in os.listdir(reel_directory):
                if filename.endswith(('.jpg', '.json', '.json.xz')):
                    os.remove(os.path.join(reel_directory, filename))

if __name__ == "__main__":
    instagram_username = input("Enter Instagram username: ")
    max_reels = int(input("Enter the number of reels you want to download: "))
    download_reels(instagram_username, max_reels)
