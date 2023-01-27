import scrapy


class FacebookSpider(scrapy.Spider):
    name = 'facebook'

    start_urls = [
            'https://www.facebook.com/cnn/',
            ]

    def parse(self, response, **kwargs):
        for post in response.css('.DShk65h2et3qCPZKn6gfgdo'):
            yield {
                'Post': post.css('.6HmzNSdANL9CF3dEbTMeBTx::text').get(),
                'Likes': post.css('.6nWzNSdANL9CF1hEbTMeBCx._3a2ZHWaih05DgAOtvu6cIo').get(),
                'Reactions': post.css('.css-F1hEbTMeBCx._3a2ZHWaih05DgAOtvu6cIo').get(),
                'Shares': post.css('.css-D1hEbdgaBC3').get(),
                'Username':post.css('.FHCV02u6Cp2zYL0fhQPsO::text').get()
                }