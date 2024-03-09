import os.path

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

NOME_VARIAVEL_CHAVE = "CHAVE_DA_SUBSCRICAO"
LOCAL_VISION = os.environ.get(
    "LOCAL_DA_SUBSCRICAO", "eastus")

IMAGES_FOLDER = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "images")


def analise_imagem(subscription_key):
    """
    Analisando a imagem e trazendo o resultado
    """
    client = ComputerVisionClient(
        endpoint="https://" + LOCAL_VISION + ".api.cognitive.microsoft.com/",
        credentials=CognitiveServicesCredentials(subscription_key)
    )

    with open(os.path.join(IMAGES_FOLDER, "tigre.jpg"), "rb") as image_stream:
        image_analysis = client.analyze_image_in_stream(
            image=image_stream,
            visual_features=[
                VisualFeatureTypes.image_type,  
                VisualFeatureTypes.faces,      
                VisualFeatureTypes.categories, 
                VisualFeatureTypes.color,      
                VisualFeatureTypes.tags,       
                VisualFeatureTypes.description
            ]
        )

    print("Essa imagem pode ser descrita como: {}\n".format(
        image_analysis.description.captions[0].text))

    print("Tags associadas:\nTag\t\tConfidence")
    for tag in image_analysis.tags:
        print("{}\t\t{}".format(tag.name, tag.confidence))

    print("\nCores dominantes: {}".format(
        image_analysis.color.dominant_colors))

    
    
    
    
    
    
    
    
    
    
    
    
    
    

if __name__ == "__main__":
    import sys, os.path
    sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
    from samples.tools import execute_samples
    execute_samples(globals(), NOME_VARIAVEL_CHAVE)
