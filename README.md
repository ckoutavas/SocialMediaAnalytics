# SocialMediaAnalytics
A python API wrapper for the Meta Graph API to pull social media post analytics over time for your connected Facebook and Instagram business accounts
## fb_published_post
If you use the metric `likes.summary(total_count)` note that "total_count represents the approximate number of nodes on the likes edge. The actual number of results returned might be different depending on privacy settings."
```
from SocialMediaAnalytics import SocialMedia


meta = SocialMedia.Meta(user_token='your_meta_access_token')
fb = meta.fb_published_post(metrics=['created_time', 'permalink_url',
                                     'message', 'likes.summary(total_count)'],
                            since='2023-03-01',
                            limit=10)
```

You can create a `pandas.DataFrame` from the above dict by doing something like:
```
fb_dfs = {list(data.keys())[0]: pd.json_normalize(data[list(data.keys())[0]]['published_posts']['data'])
          for data in fb}
# access each Facebook page's DataFrame by calling the name of the page
print(fb_dfs['Facebook Page Name'])
```

## ig_media
```
from SocialMediaAnalytics import SocialMedia


meta = SocialMedia.Meta(user_token='your_meta_access_token')
ig = meta.ig_media(metrics=['timestamp', 'media_url', 'caption', 'like_count'],
                   since='2023-03-01',
                   limit=10)
```
You can create a `pandas.DataFrame` from the above dict by doing something like:
```
ig_dfs = {list(data.keys())[0]: pd.DataFrame(data[list(data.keys())[0]]['data']) for data in ig}
# access each Instagram page's DataFrame by calling the name of the page
print(ig_dfs['Instagram Page Name'])
```
