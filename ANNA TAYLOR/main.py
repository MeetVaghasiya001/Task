from request_data import * 
from lxml import html
import json
from model import Product

all_data = request('https://www.anntaylor.com/clothing/jackets-and-blazers/cata000017/weekend-crew-neck-jacket/847520.html?priceSort=DES')

tree = html.fromstring(all_data)

script = tree.xpath("//script[@type='application/ld+json' and contains(text(),'ProductGroup')]/text()")

for i in script:
    page_data = json.loads(i)

product_name = page_data.get('name')
product_description= page_data.get('description')
product_url = page_data.get('url')
product_brand = page_data.get('brand').get('name')
product_id = page_data.get('productGroupID')
suugested_gender = page_data.get('audience').get('suggestedGender')

product_details ={}

product_varients = [{
            'sku':variant.get('sku'),
            'color':variant.get('color'),
            'price':variant.get('offers').get('price'),
            'currency':variant.get('offers').get('priceCurrency')
                } 
            for variant in page_data.get('hasVariant') if page_data.get('hasVariant')]

product_images=tree.xpath("//div[@class='carousel-item-a product-main main-image']/img/@src")
selected_size =tree.xpath("string(//span[contains(@class,'selectedFitType')]/text())").strip()

pdp_table = tree.xpath("//table[contains(@class,'ds-pdp-details')]/tr")

for p in pdp_table:
    product_details[
    p.xpath("string(.//td//h2[contains(@class,'ds-product-detail-title')])").strip()] = "".join(v.strip() for v in p.xpath(".//td[contains(@class,'ds-product-detail-des')]//text()") if v.strip())
all_size=tree.xpath("//div[@class='productFitSets ds-size-type-swatches']/a/text()")
reviews=tree.xpath("string(//div[@class='pdp-review-section-sub-left']/span/text())")
rating = tree.xpath("string(//div[@class='ratings pull-right']//span//text())")

clean_page_data={
    'product_catagory_id':product_id,
    'name':product_name,
    'brand':product_brand,
    'suggested_gender':suugested_gender,
    'images':product_images,
    'all_size':all_size,
    'selected_size':selected_size,
    'description':product_description,
    'product_detailes':product_details,
    'rating':rating,
    'reviews':reviews,
    'product_varients':product_varients
}

validate = Product(**clean_page_data)
with open('clean.json','w',encoding='utf-8') as f:
    json.dump(validate.model_dump(),f,indent=4,default=str)