from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class Drogueria(Item):

    
    nombre = Field()
    id = Field()
    #ciudad = Field() 
    #direccion = Field()
    #telefono = Field()


class DrogueriaCafam(Spider):
    name = "Drogueria Cafam"
    custom_settings = {
        "USER_AGENT" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    start_urls = ['https://www.drogueriascafam.com.co/tiendas']

    def parse(self, response):

        sel = Selector(response)
        nombres = sel.xpath('//div[@id="content-wrapper"]//article[contains(@class, "store-item card")]')
        for nombre in nombres:
            item = ItemLoader(Drogueria(), nombre)
            item.add_xpath('nombre', './/h3/text()')
            #item.add_xpath('direccion', './/' )
            item.add_value('id', 1)
        return item.load_item()