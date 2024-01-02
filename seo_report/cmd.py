import argparse
import json
import sys
import os
from six.moves.urllib import parse
from datetime import datetime

try:
    import website
except:
    from seo_report import website


def create_parser():
    parser = argparse.ArgumentParser(
        description='Analyze and report on the Search Experience of a website.'
    )

    parser.add_argument(
        '-d', '--domain', type=str, required=False,
        help='Website domain to analyze'
    )

    parser.add_argument(
        '-s', '--sitemap', type=str, required=False,
        help='Sitemap.xml file to use'
    )

    parser.add_argument(
        '-p', '--page', type=str, required=False,
        help='Single Page to analyze'
    )

    return parser


def analyze(domain, sitemap, page):
    spider = website.Spider(domain, sitemap, page)
    report = spider.crawl()

    return (json.dumps(report, indent=4, separators=(',', ': ')))


def main():
    parser = create_parser()
    args = parser.parse_args()
    print("Crawling now...")
    report = analyze(args.domain, args.sitemap, args.page)
    if (args.domain):
        parsed_url = parse.urlparse(args.domain)
    elif (args.page):
        parsed_url = parse.urlparse(args.page)

    if (not os.path.isdir('reports')):
        os.mkdir('reports')
    date_string = datetime.now().strftime('%Y-%m-%d--%H-%M-%S')
    with open('reports/%s-%s.json' % (parsed_url.netloc, date_string), 'wb') as file:
        file.write(report.encode('utf-8'))
    print("Report written. Crawl done.")


if __name__ == "__main__":
    main()
