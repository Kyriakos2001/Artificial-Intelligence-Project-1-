Τεχνητή Νοημοσύνη

Εργασία 1 Απαντήσεις

Ονοματεπώνυμο: Κυριάκος Λάμπρος Κιουράνας
Α.Μ.: 1115201900238

# Question 1

Δημιουργούμε τη στοίβα `myStack` που περιέχει πλειάδες με το πρώτο στοιχείο να είναι μία θέση και το δεύτερο έναν πίνακα που περιέχει το μονοπάτι για να φτάσουμε σε αυτή τη θέση. Σε κάθε επανάληψη, αφαιρούμε το στοιχείο από την κορυφή της στοίβας και, εφόσον δεν έχει επισκεφθεί, χρησιμοποιούμε τη συνάρτηση `getSuccessors` για να πάρουμε τους κόμβους στους οποίους μπορούμε να φτάσουμε από την τρέχουσα θέση. Τους προσθέτουμε στη στοίβα με το αντίστοιχο μονοπάτι. Αυτό συνεχίζεται μέχρι να φτάσουμε στον στόχο, οπότε και επιστρέφουμε το ζητούμενο μονοπάτι. Ο αλγόριθμος DFS χρησιμοποιεί τη στρατηγική LIFO (Last In, First Out), καθώς επιλέγουμε το τελευταίο στοιχείο που προστέθηκε στη στοίβα για το επόμενο βήμα, ακολουθώντας μια προσπέλαση κατά βάθος.

# Question 2

Στο δεύτερο ερώτημα, ακολουθούμε την ίδια διαδικασία, με τη διαφορά ότι χρησιμοποιούμε ουρά. Για την προσπέλαση κατά πλάτος, κατά την εισαγωγή από τη συνάρτηση `getSuccessors`, δεν ακολουθούμε άμεσα τα στοιχεία που εισάγουμε. Αντίθετα, ακολουθούμε τα στοιχεία που έχουν προστεθεί από προηγούμενες επαναλήψεις, δηλαδή το στοιχείο που μπήκε πρώτο θα εξεταστεί πρώτο (FIFO - First In, First Out). Αυτό εξασφαλίζει ότι προσπελαύνουμε όλα τα επίπεδα της αναζήτησης πριν προχωρήσουμε στα επόμενα.

# Question 3

Για τον αλγόριθμο `uniformCostSearch`, ακολουθούμε την ίδια διαδικασία με το δεύτερο ερώτημα, με τη διαφορά ότι χρησιμοποιούμε ουρά προτεραιότητας (Priority Queue). Χρησιμοποιούμε την ουρά προτεραιότητας, διότι θέλουμε να επιλέγουμε κάθε φορά τον κόμβο με το μικρότερο κόστος. Το κόστος αυτό καθορίζει την προτεραιότητα των κόμβων, με αποτέλεσμα το στοιχείο με το μικρότερο κόστος να βρίσκεται πάντα στην αρχή της ουράς και να επιλέγεται πρώτο.

# Question 4

Για τον αλγόριθμο `aStarSearch`, δεχόμαστε μία ευρετική συνάρτηση `heuristic` για να βελτιώσουμε τον αλγόριθμο του `uniformCostSearch`. Χρησιμοποιούμε επίσης ουρά προτεραιότητας, με τη διαφορά ότι οι κόμβοι που έχουν προτεραιότητα επιλέγονται σύμφωνα με τη συνάρτηση `heuristic` σε συνδυασμό με το κόστος. Με την κατάλληλη ευρετική συνάρτηση, μπορούμε να πετύχουμε πιο αποδοτική αναζήτηση, καθώς οι κόμβοι με την καλύτερη προοπτική βρίσκονται πάντα στην αρχή της ουράς.

# Question 5

Για την υλοποίηση του `CornersProblem`, έγιναν οι εξής ενέργειες:
- `getStartState(self)`: Η μέθοδος επιστρέφει την αρχική κατάσταση του Pacman, δηλαδή την αρχική του θέση και την κατάσταση των γωνιών, η οποία είναι αρχικά `(False, False, False, False)`.
- `isGoalState(self, state)`: Στόχος είναι να επισκεφτούμε όλες τις γωνίες. Επιστρέφει `True` αν κάθε στοιχείο της κατάστασης των γωνιών είναι `True`.
- `getSuccessors(self, state)`: Αν το επόμενο βήμα δεν είναι τοίχος, ο Pacman προχωράει και αν το επόμενο βήμα είναι μία από τις τέσσερις γωνίες, αλλάζει την κατάσταση της γωνίας σε `True`.

# Question 6

Για την υλοποίηση της ευρετικής συνάρτησης `cornersHeuristic`, χρησιμοποιούμε την απόσταση Manhattan για να επιλέξουμε την πλησιέστερη γωνία. Η ευρετική αυτή είναι `admissible` και `consistent`, καθώς το κόστος κάθε κίνησης είναι το πολύ ίσο με την απόσταση Manhattan. Για κάθε γωνία, εκτελούμε τον αλγόριθμο χρησιμοποιώντας την απόσταση Manhattan και επιλέγουμε την τιμή που είναι μεγαλύτερη, ώστε να έχουμε μια αποδεκτή και συνεπή ευρετική συνάρτηση.

# Question 7

Για την υλοποίηση της ευρετικής συνάρτησης `foodHeuristic`, χρησιμοποιούμε τη συνάρτηση `mazeDistance` για να επιλέξουμε την κοντινότερη τροφή από την τρέχουσα θέση. Η συνάρτηση `mazeDistance` είναι `admissible` και `consistent`, καθώς το κόστος κάθε κίνησης είναι 1. Εκτελούμε τον αλγόριθμο για κάθε τροφή και το ζητούμενο είναι η μέγιστη τιμή, καθώς αυτή είναι η πλέον αποδοτική στρατηγική.

# Question 8

Υλοποιούμε τη συνάρτηση `findPathToClosestDot` χρησιμοποιώντας τον αλγόριθμο `breadthFirstSearch`. Παρατηρούμε ότι, λόγω της σειράς προσπέλασης, ο Pacman μπορεί να αφήσει κάποια τρόφιμα πίσω του και αργότερα να αναγκαστεί να γυρίσει για να τα καταναλώσει. Αυτές οι κινήσεις είναι άσκοπες και δεν ανήκουν σε μια βέλτιστη διαδρομή.
