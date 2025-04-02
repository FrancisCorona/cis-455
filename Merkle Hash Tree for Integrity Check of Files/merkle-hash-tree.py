import hashlib
import sys

''' Owner: Francis Corona
    Project: Merkle Hash Tree for Integrity Check of Files
    Due: 4/2/25
'''

class merklehashTree:
    # Initialize Merkle Tree with list of file paths
    def __init__(self, filePaths):
        self.filePaths = filePaths
        self.tree = []

    # Compute the MD5 hash of given data
    def computeHash(self, data):
        return hashlib.md5(data).hexdigest()

    # Generate MD5 hash of a files content
    def hashFile(self, filePath):
        hasher = hashlib.md5()
        try:
            # Open file in binary read mode
            with open(filePath, 'rb') as f:
                # Read file in chunks to manage large files efficiently
                for chunk in iter(lambda: f.read(4096), b""):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception as e:
            # Handle errors if file cannot be read
            print(f"Error reading file {filePath}: {e}")
            return None

    # Construct Merkle Tree from file hashes
    def buildTree(self):
        # Generate hashes for all input files
        leafHashes = [self.hashFile(file) for file in self.filePaths if self.hashFile(file)]
        self.tree = leafHashes
        # Build tree upwards until one root hash remains
        while len(leafHashes) > 1:
            nextLevel = []  # Store combined hashes for next level
            for i in range(0, len(leafHashes), 2):
                left = leafHashes[i]
                right = leafHashes[i+1] if i+1 < len(leafHashes) else left
                # Combine hashes of left and right children
                combinedHash = self.computeHash((left + right).encode())
                nextLevel.append(combinedHash)
            leafHashes = nextLevel
            self.tree.extend(leafHashes)

    # Retrieve top hash of Merkle Tree
    def gettopHash(self):
        return self.tree[-1] if self.tree else None

if __name__ == "__main__":
    # Get list of file paths from command line arguments
    files = sys.argv[1:]
    if not files:
        print("Usage: python merkle-hash-tree.py <file1> <file2> ...")
        exit(1)

    # Create instance of Merkle Tree
    merkleTree = merklehashTree(files)
    # Build tree and calculate top hash
    merkleTree.buildTree()
    topHash = merkleTree.gettopHash()
    
    if topHash:
        print(f"Top Hash: {topHash}")
    else:
        print("Error computing top hash.")
