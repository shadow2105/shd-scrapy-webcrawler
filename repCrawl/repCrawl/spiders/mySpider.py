# See: https://docs.scrapy.org/en/latest/

import scrapy
from ..items import RepcrawlItem


# scrapy.Spider - Base class for scrapy spiders.
# All spiders must inherit from this class.
class MySpider(scrapy.Spider):

    # Spider name attribute (string) is how the spider is located (and instantiated) by Scrapy,
    # so it must be unique.
    name = "mySpider"

    # Optional; Requests for URLs not belonging to the domain names specified in this list
    # (or their subdomains) won’t be followed if OffsiteMiddleware is enabled.
    allowed_domains = ['house.gov']

    # Method called (once) by Scrapy when the spider is opened for scraping.
    # safe to implement as a generator.
    def start_requests(self):

        #  list of URLs where the spider will begin to crawl from.
        start_urls = ['https://www.house.gov/representatives', ]

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
            # A Request object represents an HTTP request,
            # usually generated in the Spider and executed by the Downloader, and thus generating a Response.

        # return super().start_requests()

    # Method in charge of processing the response and returning scraped data and/or more URLs to follow
    def parse(self, response, *args, **kwargs):

        # creating items dictionary; as per the fields/keys defined in ..\items.py --> class RepcrawlItem
        items = RepcrawlItem()

        # CSS Selector to extract Names;
        #   <table class="table" id="housegov_reps_by_name-block_default-523676408">
        #       <td headers="view-value-1-table-column" class="views-field views-field-value-1 views-field-value-2">
        #           <a href="https://adams.house.gov">Adams, Alma</a>        </td>
        complete_names = response.css('table[id*=_reps_by_name] td[headers*=view-value-1] a ::text').getall()

        first_names = []
        last_names = []

        for name in complete_names:
            split_name = name.split(",")
            first_names.append(split_name[0])
            last_names.append(split_name[1].strip())
            # split_name[0] is the actual lastname and split_name[1] is the firstname.
            # above code is to present data like sample.json

        # CSS Selector to extract Districts;
        #   <td headers="view-value-4-table-column--57" class="views-field views-field-value-3
        #    views-field-value-4">North Carolina 12th        </td>
        districts = [dsct.strip() for dsct in
                     response.css('table[id*=_reps_by_name] td[headers*=view-value-4] ::text').getall()]

        # CSS Selector to extract Parties;
        #   <td headers="view-value-6-table-column" class="views-field views-field-value-6">D        </td>
        parties = [pty.strip() for pty in
                   response.css('table[id*=_reps_by_name] td[headers*=view-value-6] ::text').getall()]

        # CSS Selector to extract Rooms;
        #   <td headers="view-value-8-table-column" class="views-field views-field-value-7
        #    views-field-value-8">2436 RHOB        </td>
        rooms = [rm.strip() for rm in
                 response.css('table[id*=_reps_by_name] td[headers*=view-value-8] ::text').getall()]

        # CSS Selector to extract Phones;
        #   <td headers="view-value-9-table-column--57" class="views-field
        #    views-field-value-9">(202) 225-1510        </td>
        phones = [pn.strip() for pn in
                  response.css('table[id*=_reps_by_name] td[headers*=view-value-9] ::text').getall()]

        # CSS Selector to extract Committee Assignments;
        #  <td headers="view-markup-table-column--57" class="views-field views-field-markup">
        #       <ul><li>Agriculture</li><li>Financial Services</li><li>Education and Labor</li></ul>        </td>
        tds_comm_assigns = response.css('table[id*=_reps_by_name] td[headers*=view-markup]')

        committee_assignments = []

        for td in tds_comm_assigns:
            ul_elements = td.css('ul li ::text').getall()
            committees = " ".join(ul_elements)
            committee_assignments.append(committees)

        # Type and Country field explicitly defined; not found in page source.
        typ = "Federal"

        country = "United State Of America"

        url = "https://www.house.gov/representatives"
        # To extract URL of each house representative, use the CSS Selector as shown below -
        # rep_url = response.css('table[id*=_reps_by_name] td[headers*=view-value-1] a::attr(href)').getall()

        rep_data = zip(first_names, last_names, districts, parties, rooms, phones, committee_assignments)
        # rep_data = []
        # for i in range(len(first_names)):
        #     rep_data.append((first_names[i], last_names[i], districts[i], parties[i], rooms[i], phones[i],
        #                      committee_assignments[i]))

        for firstName, lastName, district, party, room, phone, committeeAssignment in rep_data:
            items["firstname"] = firstName
            items["lastname"] = lastName
            items["district"] = district
            items["party"] = party
            items["room"] = room
            items["phone"] = phone
            items["committeeAssignment"] = committeeAssignment
            items["type"] = typ
            items["country"] = country
            items["url"] = url

            yield items

            # yield {
            #
            #     "firstname": firstName,
            #     "lastname": lastName,
            #     "district": district,
            #     "party": party,
            #     "room": room,
            #     "phone": phone,
            #     "committeeAssignment": committeeAssignment,
            #     "type": typ,
            #     "country": country,
            #     "url": url
            #
            # }

            # if 'house.gov' in url:
            #     yield scrapy.Request(url=url, callback=self.parse)
