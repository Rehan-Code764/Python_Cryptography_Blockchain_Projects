
import hashlib
import time


class Block:
    def __init__(self, index, voter_id, vote, previous_hash):
        self.index = index
        self.voter_id = voter_id
        self.timestamp = time.time()
        self.vote = vote
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = (
            str(self.index)
            + str(self.timestamp)
            + str(self.voter_id)
            + str(self.vote)
            + str(self.previous_hash)
        )
        return hashlib.sha256(value.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.votes = set()
        self.candidates = set()

    def create_genesis_block(self):
        return Block(0, "Genesis", "None", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_candidate(self, candidate_name):
        candidate_name = candidate_name.strip()

        if not candidate_name:
            print("Candidate name cannot be empty.")
        elif candidate_name in self.candidates:
            print("Candidate already exists.")
        else:
            self.candidates.add(candidate_name)
            print(f"Candidate {candidate_name} added successfully.")

    def cast_vote(self, voter_id, candidate_name):
        voter_id = voter_id.strip()
        candidate_name = candidate_name.strip()

        if not voter_id:
            print("Voter ID cannot be empty.")
            return False

        if voter_id in self.votes:
            print("Voter has already cast their vote.")
            return False

        if candidate_name not in self.candidates:
            print("Invalid candidate.")
            return False

        latest_block = self.get_latest_block()

        new_block = Block(
            len(self.chain),
            voter_id,
            candidate_name,
            latest_block.hash
        )

        self.chain.append(new_block)
        self.votes.add(voter_id)

        print(f"Vote cast successfully for {candidate_name}.")
        return True

    def get_vote_count(self):
        vote_count = {
            candidate: 0 for candidate in self.candidates
        }

        for block in self.chain[1:]:
            if block.vote in vote_count:
                vote_count[block.vote] += 1

        return vote_count

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def display_candidates(self):
        if not self.candidates:
            print("No candidates available.")
            return

        print("\nAvailable Candidates:")
        for candidate in sorted(self.candidates):
            print("-", candidate)

    def display_blockchain(self):
        for block in self.chain:
            print("\n------------------------------")
            print("Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Voter ID:", block.voter_id)
            print("Vote:", block.vote)
            print("Hash:", block.hash)
            print("Previous Hash:", block.previous_hash)

        print("------------------------------")


def main():
    blockchain = Blockchain()

    while True:
        print("\n===== BLOCKCHAIN VOTING SYSTEM =====")
        print("1. Add Candidate")
        print("2. Show Candidates")
        print("3. Cast Vote")
        print("4. Show Vote Count")
        print("5. Check Blockchain Validity")
        print("6. Display Blockchain")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            name = input("Enter candidate name: ")
            blockchain.add_candidate(name)

        elif choice == "2":
            blockchain.display_candidates()

        elif choice == "3":
            if not blockchain.candidates:
                print("Please add candidates first.")
                continue

            voter_id = input("Enter voter ID: ")

            blockchain.display_candidates()
            candidate = input("Enter candidate name to vote for: ")

            blockchain.cast_vote(voter_id, candidate)

        elif choice == "4":
            results = blockchain.get_vote_count()

            if not results:
                print("No candidates registered yet.")
            else:
                print("\n===== VOTING RESULTS =====")
                for candidate, count in sorted(results.items()):
                    print(f"{candidate}: {count} votes")

        elif choice == "5":
            if blockchain.is_chain_valid():
                print("Blockchain is valid.")
            else:
                print("Blockchain is NOT valid!")

        elif choice == "6":
            blockchain.display_blockchain()

        elif choice == "7":
            print("Thank you for using Blockchain Voting System!")
            break

        else:
            print("Invalid option! Please choose between 1 and 7.")


if __name__ == "__main__":
    main()
