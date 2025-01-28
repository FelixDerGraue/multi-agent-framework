import asyncio
from magent.agents.ai_tracker import AINewsTracker
from magent.collectors.ai_news_collector import AINewsCollector

async def main():
    # Initialize the AI tracking system
    api_keys = {
        'arxiv': 'your_arxiv_key',
        'news_api': 'your_news_api_key',
        'twitter': 'your_twitter_api_key',
    }
    
    # Create the collector and tracker
    collector = AINewsCollector(api_keys)
    tracker = AINewsTracker('ai_trends_tracker', [
        'large_language_models',
        'computer_vision',
        'reinforcement_learning',
        'ai_ethics',
        'ai_infrastructure'
    ])

    # Configure tracking parameters
    keywords = [
        'artificial intelligence',
        'machine learning',
        'deep learning',
        'neural networks',
        'AI research',
        'LLM',
        'transformer models',
        'AI ethics',
    ]

    # Collect data from different sources
    research_papers = await collector.collect_research_papers(timeframe_days=7)
    news_items = await collector.collect_industry_news(keywords)
    social_trends = await collector.collect_social_trends()

    # Process collected data
    for paper in research_papers:
        tracker.process_news_item(paper)
    
    for news in news_items:
        tracker.process_news_item(news)
    
    for platform, trends in social_trends.items():
        for trend in trends:
            tracker.process_news_item({
                'source': platform,
                'type': 'social_trend',
                'content': trend
            })

    # Generate insights
    trending_topics = tracker.get_trending_topics(timeframe_days=7)
    insight_report = tracker.generate_insight_report()

    # Print insights
    print("\n=== AI Industry Trends Report ===\n")
    
    print("Top Trending Topics by Category:")
    for category, topics in trending_topics.items():
        print(f"\n{category.replace('_', ' ').title()}:")
        for topic in topics[:3]:  # Top 3 topics per category
            print(f"- {topic['title']}")
            print(f"  Impact Score: {topic['impact_score']}")

    print("\n=== Key Insights ===")
    for insight in insight_report['key_trends']:
        print(f"\n- {insight['title']}")
        print(f"  {insight['description']}")

    print("\n=== Emerging Technologies ===")
    for tech in insight_report['emerging_technologies']:
        print(f"\n- {tech['name']}")
        print(f"  Potential Impact: {tech['impact']}")
        print(f"  Maturity: {tech['maturity']}")

    print("\n=== Strategic Recommendations ===")
    for rec in insight_report['recommendations']:
        print(f"\n- {rec}")

if __name__ == "__main__":
    asyncio.run(main())