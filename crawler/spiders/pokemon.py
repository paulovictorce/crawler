import scrapy


class PokemonSpider(scrapy.Spider):
    name = 'pokemon'

    def start_request(self):
        yield scrapy.Request(url='https://pokemondb.net/pokedex/national', callback=self.parse)

    def parse(self, response):
        identificador = response.css('span.infocard-tall small::text').extract_first()
        nome = response.css('span.infocard-tall .ent-name::text').extract_first()
        tipo = response.css('span.infocard-tall small.aside::text').extract_first()
        self.log('Name : %s' % nome)
        self.log('Id : %s' % identificador)
        self.log('Tipo : %s' % tipo)
