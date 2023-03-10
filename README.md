# SocialMediaAnalytics
A python API wrapper for the Meta Graph API to pull social media post analytics over time for your connected Facebook and Instagram business accounts
## fb_published_posts
### published_posts endpoint field values to be used with the `metrics` param
Note that this is not a full list of fileds for the published_posts endpoint.

If you use `likes.summary(total_count)` note that "total_count represents the approximate number of nodes on the likes edge. The actual number of results returned might be different depending on privacy settings."

- actions
- admin_creator
- comments{}
  - message
  - name
  - username
- created_time
- from
- full_picture
- is_eligible_for_promotion
- instagram_eligibility
- id
- is_expired
- is_hidden
- is_inline_created
- is_instagram_eligible
- is_popular
- is_published
- likes.summary(total_count)
- message
- message_tags
- permalink_url
- reactions{}
  - username
  - type
- likes{}
  - name
  - username
- likes.summary(total_count)

### fb.published_posts example

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
### Media endpoint field values to be used with the `metrics` param
Note that this is not a full list of fileds for the ig_media endpoint.
- caption
- comments{}
  - text
  - like_count
  - from
  - hidden
  - id
  - media
  - parent_id
  - timestamp
  - user
  - username
- comments_count
- id
- ig_id
- is_comment_enabled
- is_shared_to_feed
- like_count
- media_product_type
- media_type
- media_url
- owner
- permalink
- shortcode
- thumbnail_url
- timestamp
- username

### ig_media example
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

