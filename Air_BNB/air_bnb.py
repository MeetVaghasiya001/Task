
import json
from pydantic import BaseModel
from typing import List, Dict, Optional


class ImageModel(BaseModel):
    image_type: Optional[str]
    imageUrl: List[str]


class HighlightModel(BaseModel):
    title: Optional[str]
    sub_title: Optional[str]


class AmenitiesModel(BaseModel):
    title: str
    amenities: List[str]





class PropertyModel(BaseModel):
    room: Optional[str]
    location: Optional[str]
    images: List[ImageModel] = []
    highlights: List[HighlightModel] = []
    nearby_locations: List[str] = []
    overall_rating: Optional[float]
    review_count : Optional[int]
    amenities: List[AmenitiesModel] = []
    rules: List[str] = []
    host: Optional[str]
    description: Optional[str]


with open('air_bnb.json','r',encoding='utf-8') as f:
    all_data = json.load(f)

path = all_data.get('niobeClientData',{})
main_path = path[0][1].get('data',{}).get('presentation',{}).get('stayProductDetailPage',{}).get('sections',{}).get('sections',{})


for s in main_path:
    if s.get('sectionId',{}) == 'AVAILABILITY_CALENDAR_INLINE':
        room = s.get('section',{}).get('listingTitle',{})
        location = s.get('section',{}).get('localizedLocation',{})

       
    if s.get('sectionId',{}) == 'PHOTO_TOUR_SCROLLABLE_MODAL':
        images = s.get('section').get('mediaItems')
        ids = s.get('section').get('roomTourLayoutInfos')[0].get('roomTourItems')
        id_titles = []
        for id in ids:
            title = id.get('title')
            all_id = id.get('imageIds')
            id_titles.append({
                'title':title,
                'id':all_id
            })
        urls = []
        for titles in id_titles:
            for image in images:
                if titles.get('title') in image.get('accessibilityLabel'):
                    if titles.get('title') not in urls:
                        urls.append({
                        titles.get('title'):[image.get('baseUrl')]
                        })
        

        
        
        

    if s.get('sectionId',{}) == 'HIGHLIGHTS_DEFAULT':
        highlights = s.get('section',{}).get('highlights',{})
        all_hlt = []
        for hlt in highlights:
            all_hlt.append({
                'title':hlt.get('title'),
                'sub_title':hlt.get('subtitle')
            })


    if s.get('sectionId',{}) == 'SEO_LINKS_DEFAULT':
        other_loc = s.get('section',{}).get('nearbyCities',{})
        all_loc = {'other_locations':[loc.get('title',{}) for loc in other_loc]}
        
    if s.get('sectionId',{}) == 'REVIEWS_DEFAULT':
        ratings = s.get('section',{}).get('ratings',{})
        overall_rating = s.get('section',{}).get('overallRating',{})
        review_count = s.get('section',{}).get('overallCount',{})


    if s.get('sectionId',{}) == 'AMENITIES_DEFAULT':
        all_aminities = s.get('section',{}).get('seeAllAmenitiesGroups',{})
        all_amt =[]
        for amt in all_aminities:
            all_amt.append({
                'title':amt.get('title'),
                'amenities':[aamt.get('title') for aamt in amt.get('amenities')]
            })

            
    if s.get('sectionId',{}) == 'POLICIES_DEFAULT':
        rules = s.get('section',{}).get('houseRules',{})
        all_rule =[rule.get('title') for rule in rules]
            

    if s.get('sectionId',{}) == 'MEET_YOUR_HOST':
        host = s.get('section',{}).get('cardData',{}).get('name',{})

    if s.get('sectionId',{}) == 'DESCRIPTION_DEFAULT':
        discription= s.get('section',{}).get('htmlDescription',{}).get('htmlText',{})




data = {
    'room':room,
    'location':location,
    'images':urls,
    'highlights':all_hlt,
    'nearby_locations':all_loc['other_locations'],
    'overall_rating':overall_rating,
    'review_count':review_count,
    'amenities':all_amt,
    'rules':all_rule,
    'host':host,
    'description':discription
}


check = PropertyModel(**data)

with open('clean.json','w') as v:
    json.dump(check.model_dump(),v,indent=4,default=str)















            