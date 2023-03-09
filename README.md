# SocialMediaAnalytics
A python API wrapper to gather social media post analytics over time for your connected Facebook and Instagram business accounts
## fb_published_post
```
from SocialMediaAnalytics import SocialMedia


meta = SocialMedia.Meta(user_token='your_meta_access_token')
fb = meta.fb_published_post(metrics=['created_time', 'permalink_url',
                                     'message', 'likes.summary(total_count)'],
                            since='2023-03-01',
                            limit=10)
```

## ig_media
```
from SocialMediaAnalytics import SocialMedia


meta = SocialMedia.Meta(user_token='your_meta_access_token')
ig = meta.ig_media(metrics=['timestamp', 'media_url', 'caption', 'like_count'],
                   since='2023-03-01',
                   limit=10)
```
