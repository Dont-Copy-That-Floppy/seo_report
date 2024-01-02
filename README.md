[![Build Status](https://travis-ci.org/drawbuildplay/seo_report.svg?branch=master)](https://travis-ci.org/drawbuildplay/seo_report)
[![Coverage Status](https://coveralls.io/repos/github/drawbuildplay/seo_report/badge.svg?branch=master)](https://coveralls.io/github/drawbuildplay/seo_report?branch=master)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/drawbuildplay/seo_report/master/LICENSE)

SEO Report
==========
Updated by ya boi to work with zero install, single page, site fixes, and produce a json file report. Later going to add an interface to produce somee legit dl.... eh 👊 Clean up your room!

Scan your website for On Page Search Experience Optimization issues based on 
the SEO guidelines from Google's SEO Starter Guide:
        
http://static.googleusercontent.com/media/www.google.com/en//webmasters/docs/search-engine-optimization-starter-guide.pdf


Usage
-----

```
python seoreport\cmd.py -d http://www.domain.com
python seoreport\cmd.py -s http://www.domain.com/sitemap.xml
python seoreport\cmd.py -p http://www.domain.com/some_singular_endpoint
```

Testing (untested)
-------
```
#pip install -r tests/test-requirements.txt
#nosetests --with-coverage
```

Milestones (most from the original):
-------
Report Features:
* Calculate how much of the page is text vs images vs code.
  * There needs to be a good balance (too much images can impact what search engines can parse. Too much text is too heavy for users.)
  * Too many large images impacts page load time - especially for mobile devices.
* Display useful analytics using Charts.js
  * Score (radar)
  * Pie/Donuts for ratio levels (text vs image, broken links, etc)
  * Tag Cloud for keywords
* Data should be partitioned into logical sections so that the user can easily focus their attention on the main issues and allocate work to their team as appropriate. (somehow derive ROI??? sounds fkn hard. maybe use copilot and search for repos pertaining to fix, count the lines of code, and extrapolate???)
  
Website Analytics:
* measure page performance and use of a CDN
* Avoid having passive or negative text as that degrades the customers experience on your website.
* Who is linking back to your website. How popular are those sites?
* Are you running analytics on your website to get insights into customer behavior
* crawling of individual webpages should be done asynchronously using multiple workers. (ie multithread)
* Look at Alexa, Moz, and other major directories.
* how often does the website create new posts?
* Show screen grabs of the website analyzed.
  * Grabs should be in desktop, tablet, and mobile views.
    
Social Insights:
* Analyze the social hints about the page. How many times has it been shared etc.
  * Search Experience Optimization looks at how people are talking about this topic and provides a hint to search engines on the popularity of the topic.
