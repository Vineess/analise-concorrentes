import scrapy

class ReclameAquiSpider(scrapy.Spider):
    name = 'reclameaqui'
    allowed_domains = ['www.reclameaqui.com.br']

    def __init__(self, empresa='', *args, **kwargs):
        super(ReclameAquiSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'https://www.reclameaqui.com.br/empresa/{empresa}/']

    def parse(self, response):
        # Captura os dados da empresa
        empresa_nome = response.xpath('//h1/text()').get()
        total_reclamacoes = response.xpath('//div[contains(@class, "company-header-stats__number")]/text()').get()
        indice_empresa = response.xpath('//div[contains(@class, "company-header-stats__rating")]/text()').get()

        yield {
            'empresa': empresa_nome.strip() if empresa_nome else 'Não encontrado',
            'total_reclamacoes': total_reclamacoes.strip() if total_reclamacoes else 'Não encontrado',
            'indice_empresa': indice_empresa.strip() if indice_empresa else 'Não encontrado',
        }

        
        for reclamacao in response.css('div.reclamacao-card'):
            resposta = reclamacao.css('div.resposta::text').get()
            if not resposta:  
                titulo = reclamacao.css('h3.titulo::text').get()
                descricao = reclamacao.css('p.descricao::text').get()

                
                yield {
                    'empresa': empresa_nome.strip() if empresa_nome else 'Não encontrado',
                    'titulo': titulo.strip() if titulo else 'Não encontrado',
                    'descricao': descricao.strip() if descricao else 'Não encontrado',
                    'status': 'Sem Resposta'
                }

        
        next_page = response.xpath('//a[@class="next_page"]/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)
