import psutil
import gc
import chromadb
from datetime import datetime

class MemoryMonitor:
    def __init__(self, threshold=75):
        self.threshold = threshold
        
    def check_and_clean(self):
        usage = psutil.virtual_memory().percent
        if usage > self.threshold:
            print(f"[!] RAM at {usage}%. Triggering Garbage Collection...")
            gc.collect()

class LongTermMemory:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection(name="jarvis_history")

    def store_interaction(self, query, response):
        self.collection.add(
            documents=[f"User: {query} | Jarvis: {response}"],
            metadatas=[{"timestamp": str(datetime.now())}],
            ids=[str(datetime.now().timestamp())]
        )
