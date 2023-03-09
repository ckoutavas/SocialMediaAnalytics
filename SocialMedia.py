import requests
import datetime
from typing import List, Any, Union


class Meta:
    def __init__(self, user_token: str) -> None:
        """
        The Meta class accesses the Meta Graph API based on your user token and will pull all the page tokens
        for your business. Yu can get your page IDs and access tokens from self.page_tokens:

        meta = Meta(user_token='your_access_token')
        print(meta.page_tokens)

        :param user_token: str your meta access token
        """
        self.token = user_token  # access token

        url = f"https://graph.facebook.com/v15.0/me?fields=id%2Cname%2Caccounts&access_token={self.token}"
        page_data = requests.get(url).json()  # API json response
        # create a dict with the id and access token for all pages you manage
        self.page_tokens = {data['name']: {'id': data['id'], 'token': data['access_token']}
                            for data in page_data['accounts']['data']}

    def fb_published_post(self, metrics: List[Union[Any, str]], limit: int, **kwargs) -> List[Union[Any, dict]]:
        """
        Pulls data from published_posts

        :param metrics: list of fields for published_posts:
                        ['created_time', 'permalink_url', 'message', 'likes.summary(total_count)']
        :param limit: int max number of records to return for each business account
        :param kwargs: since or until - you can only use one
        :return: list of dicts
        """

        if kwargs:
            since = kwargs.get('since', None)
            until = kwargs.get('until', None)

            not_valid = [x for x in [*kwargs] if x not in ['since', 'until']]

            if len(not_valid) > 0:
                raise AttributeError(
                    f'{not_valid} are not valid keyword arguments. You can only use "since" or "until"')

            if since is not None and until is not None:
                raise AttributeError(f'You can only assign one of the following keywords, not both: "since" or "until"')

            fb_posts = []
            for k, v in self.page_tokens.items():
                if since:
                    post_since = datetime.datetime.strptime(since, '%Y-%m-%d').date().strftime('%s')
                    posts_url = (f"https://graph.facebook.com/{v['id']}?"
                                 f"fields=published_posts.limit({limit})"
                                 f".since({post_since})"
                                 "{" + f"{','.join(metrics)}" + "}"
                                                                f"&access_token={v['token']}")

                    post_resp = requests.get(posts_url).json()
                    fb_posts.append({k: post_resp})

                if until:
                    post_until = datetime.datetime.strptime(until, '%Y-%m-%d').date().strftime('%s')
                    posts_url = (f"https://graph.facebook.com/{v['id']}?"
                                 f"fields=published_posts.limit({limit})"
                                 f".until({post_until})"
                                 "{"
                                 f"{','.join(metrics)}"
                                 "}"
                                 f"&access_token={v['token']}")
                    post_resp = requests.get(posts_url).json()
                    fb_posts.append({k: post_resp})
            return fb_posts

        else:
            fb_posts = []
            for k, v in self.page_tokens.items():
                posts_url = (f"https://graph.facebook.com/{v['id']}?"
                             f"fields=published_posts.limit({limit})"
                             "{"
                             f"{','.join(metrics)}"
                             "}"
                             f"&access_token={v['token']}")
                post_resp = requests.get(posts_url).json()
                fb_posts.append({k: post_resp})

            return fb_posts

    def ig_media(self, metrics: List[str], since: str,  limit: int) -> List[Union[Any, dict]]:
        """
        Pulls data from media

        :param metrics: list of fields for media:
                        ['timestamp', 'media_url', 'caption', 'like_count']
        :param since: str date in yyyy-mm-dd format to pull data from this date forward
        :param limit: int max number of records to return for each busness account
        :return: list of dicts
        """
        since = datetime.datetime.strptime(since, '%Y-%m-%d').date().strftime('%s')
        ig_media = []
        for k, v in self.page_tokens.items():
            ig_biz_url = (f"https://graph.facebook.com/v15.0/{v['id']}?"
                          f"fields=instagram_business_account%7Busername%2Cmedia_count%7D"
                          f"&access_token={v['token']}")

            ig_data = requests.get(ig_biz_url).json()
            media_url = (f"https://graph.facebook.com/v15.0/{ig_data['instagram_business_account']['id']}/media?"
                         f"fields={','.join(metrics)}"
                         f"&limit={limit}"
                         f"&since={since}"
                         f"&access_token={v['token']}")

            media_resp = requests.get(media_url).json()
            ig_media.append({k: media_resp})
        return ig_media
