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
