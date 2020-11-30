from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda

with Diagram("The Secret Formula", show=False):
    with Cluster("Who?"):
        whoQuestions = [
            Lambda("Who is your dream client?"),
            Lambda("Who do I actually want to work with?"),
            Lambda("What are they passionate about?"),
            Lambda("What are their goals, dreams, and desires?")
        ]

    with Cluster("Where?"):
        whereQuestions = [
            Lambda("Where can you find your dream clients?"),
            Lambda("What groups are they a part of?"),
            Lambda("What interests do they have?"),
            Lambda("Where do they hang out online?")
        ]

    with Cluster("Bait?"):
        baitQuestions = [
            Lambda("What bait will you use to attract your dream clients?"),
            Lambda("Is your bait a physical book?"),
            Lambda("Is your bait a CD?"),
            Lambda("Is your bait an audio file?")
        ]

    with Cluster("Result?"):
        resultQuestions = [
            Lambda("What result do you want to give your dream clients?")
        ]

    Lambda("Who?") >> whoQuestions >> Lambda("Where?") >> whereQuestions >> Lambda("Bait?") >> baitQuestions >> Lambda("Result?") >> resultQuestions
