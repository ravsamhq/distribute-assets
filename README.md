[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Distribute Assets on CDN

Distribute your website assets quickly on a CDN after deployment

## Problem to Solve

If you are using Neltify or other JAMstack based platforms, you know that on each deployment your website cache is invalidated. After a new deployment, a lazy distribution approach is used by these platforms to distribute your assets. Assets are distributed only when a they are accessed by the client. This results in slow response time after new deployments. This action solves this problem by send sending `GET` requests to all the assets on your website which leads the hosting platforms to distribute them to CDNs around the world.

## Example workflow

```yaml
steps:
  - uses: ravsamhq/distribute-assets@master
    with:
      sitemap_url: # https://example.com/sitemap.xml
```

> Made in Python &bull; By [Ravgeet Dhillon](https://github.com/ravgeetdhillon) @ [RavSam Web Solutions](https://www.ravsam.in).
