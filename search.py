# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # Αρχικοποίηση μιας στοίβας για το σύνορο, ξεκινώντας από την αρχική κατάσταση, έναν κενό δρόμο και αρχικό κόστος 0
    frontier = util.Stack()
    # Η στοίβα περιέχει πλειάδες (κατάσταση, διαδρομή)
    frontier.push((problem.getStartState(), []))  

    # Σύνολο για την παρακολούθηση των επισκέψεων στις καταστάσεις
    visited = set()

    while not frontier.isEmpty():
        # Λήψη της τρέχουσας κατάστασης και διαδρομής από τη στοίβα
        current_state, current_path = frontier.pop()

        # Έλεγχος αν έχουμε φτάσει στον στόχο
        if problem.isGoalState(current_state):
            return current_path

        # Αν η τρέχουσα κατάσταση δεν έχει επισκεφθεί ακόμα
        if current_state not in visited:
            # Σημειώστε την τρέχουσα κατάσταση ως επισκεφθείσα
            visited.add(current_state)

            # Επέκταση της τρέχουσας κατάστασης και προσθήκη κάθε διαδόχου στο σύνορο
            for successor, action, step_cost in problem.getSuccessors(current_state):
                if successor not in visited:
                    new_path = current_path + [action]
                    frontier.push((successor, new_path))

    # Αν δεν βρέθηκε λύση, επιστρέφει μια κενή λίστα
    return []

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    # Αρχικοποίηση μιας ουράς για το σύνορο, ξεκινώντας από την αρχική κατάσταση, έναν κενό δρόμο και αρχικό κόστος 0
    frontier = util.Queue()
    # Η ουρά περιέχει πλειάδες (κατάσταση, διαδρομή)
    frontier.push((problem.getStartState(), []))  

    # Σύνολο για την παρακολούθηση των επισκέψεων στις καταστάσεις
    visited = set()

    while not frontier.isEmpty():
        # Λήψη της τρέχουσας κατάστασης και διαδρομής από την ουρά
        current_state, current_path = frontier.pop()

        # Έλεγχος αν έχουμε φτάσει στον στόχο
        if problem.isGoalState(current_state):
            return current_path

        # Αν η τρέχουσα κατάσταση δεν έχει επισκεφθεί ακόμα
        if current_state not in visited:
            # Γίνεται σημείωση της τρέχουσας κατάστασης ως επισκεφθείσα
            visited.add(current_state)

            # Επέκταση της τρέχουσας κατάστασης και προσθήκη κάθε διαδόχου στο σύνορο
            for successor, action, step_cost in problem.getSuccessors(current_state):
                if successor not in visited:
                    new_path = current_path + [action]
                    frontier.push((successor, new_path))

    # Αν δεν βρέθηκε λύση, επιστρέφει μια κενή λίστα
    return []


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # Αρχικοποίηση μιας ουράς προτεραιότητας για το σύνορο με την αρχική κατάσταση, έναν κενό δρόμο και αρχικό κόστος 0
    frontier = util.PriorityQueue()
    # Η ουρά προτεραιότητας περιέχει πλειάδες (κατάσταση, διαδρομή, κόστος)
    frontier.push((problem.getStartState(), [], 0), 0)  

    # Σύνολο για την παρακολούθηση των επισκέψεων στις καταστάσεις
    visited = set()

    while not frontier.isEmpty():
        # Γινεται αφαιρεση της κατάστασης με το μικρότερο κόστος από το σύνορο
        current_state, current_path, current_cost = frontier.pop()

        # Έλεγχος αν έχουμε φτάσει στον στόχο
        if problem.isGoalState(current_state):
            return current_path

        # Αν η τρέχουσα κατάσταση δεν έχει επισκεφθεί ακόμα
        if current_state not in visited:
            # Σημειώστε την τρέχουσα κατάσταση ως επισκεφθείσα
            visited.add(current_state)

            # Επέκταση της τρέχουσας κατάστασης και προσθήκη κάθε διαδόχου στο σύνορο
            for successor, action, step_cost in problem.getSuccessors(current_state):
                if successor not in visited:
                    new_path = current_path + [action]
                    new_cost = current_cost + step_cost
                    frontier.push((successor, new_path, new_cost), new_cost)

    # Αν δεν βρέθηκε λύση, επιστρέφει μια κενή λίστα
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    # Αρχικοποίηση μιας ουράς προτεραιότητας για το σύνορο με την αρχική κατάσταση, έναν κενό δρόμο και αρχικό κόστος 0
    frontier = util.PriorityQueue()
    start_state = problem.getStartState()
    # Η ουρά προτεραιότητας περιέχει πλειάδες (κατάσταση, διαδρομή, κόστος)
    frontier.push((start_state, [], 0), heuristic(start_state, problem)) 

    # Σύνολο για την παρακολούθηση των επισκέψεων στις καταστάσεις και ένα λεξικό για την αποθήκευση του καλύτερου κόστους για κάθε κατάσταση    visited = set()
    visited = set()
    best_cost = {}

    while not frontier.isEmpty():
        # Γινεται αφαιρεση του κόμβου με το χαμηλότερο συνδυασμένο κόστος και ευρετική από το σύνορο
        current_state, current_path, current_cost = frontier.pop()

        # Έλεγχος αν έχουμε φτάσει στον στόχο
        if problem.isGoalState(current_state):
            return current_path

        # Αν η τρέχουσα κατάσταση δεν έχει επισκεφθεί ή βρέθηκε καλύτερη διαδρομή
        if current_state not in visited or current_cost < best_cost.get(current_state, float('inf')):
            # Ενημερώστε το καλύτερο κόστος για την τρέχουσα κατάσταση και σημειώστε την ως επισκεφθείσα
            best_cost[current_state] = current_cost
            visited.add(current_state)

            # Επέκταση της τρέχουσας κατάστασης και προσθήκη κάθε διαδόχου στο σύνορο
            for successor, action, step_cost in problem.getSuccessors(current_state):
                new_path = current_path + [action]
                new_cost = current_cost + step_cost
                priority = new_cost + heuristic(successor, problem)
                
                # Προσθήκη του διαδόχου στην ουρά προτεραιότητας με την υπολογισμένη προτεραιότητα
                frontier.push((successor, new_path, new_cost), priority)

    # Αν δεν βρέθηκε λύση, επιστρέφει μια κενή λίστα
    return []
    

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
