pub type Coord = (i32, i32);

/// Returns the manhattan distance
fn manhattan_dist(a: Coord, b: Coord) -> u32 {
    (b.0 - a.0).abs() as u32 + (b.1 - a.1).abs() as u32
}

pub fn move_tail(tail: &mut Coord, head: &Coord) {
    // Let's say H is 1 right of T.
    // So T.H, M_dist is 2
    // T should move 1 to the right
    // .TH, M_dist is 1
    // Done

    while manhattan_dist(*head, *tail) >= 2 {
        // Align x within 1 of each other
        // Align y within 1 of each other

        // First, handle x
        if head.0 > tail.0 {
            let dist_to_1 = head.0 - tail.0 - 1;
            println!("Moving tail up by {dist_to_1}");
            tail.0 += dist_to_1;
        }
        else if head.0 < tail.0 {
            let dist_to_1 = head.0 - tail.0 - 1;
            println!("Moving tail down by {dist_to_1}");
            tail.0 -= dist_to_1;
        }
        else {
            println!("Xs are aligned.");
        }
        // TODO do I need to check if they're equal?

        // Next, handle y
        if head.1 > tail.1 {
            let dist_to_1 = head.1 - tail.1 - 1;
            println!("Moving tail right by {dist_to_1}");
            tail.1 += dist_to_1;
        }
        else if head.1 < tail.1 {
            let dist_to_1 = head.1 - tail.1 - 1;
            println!("Moving tail left by {dist_to_1}");
            tail.1 -= dist_to_1;
        }
        else {
            println!("Xs are aligned.");
        }
    }
}


#[test]
fn test_manhattan() {
    assert_eq!(manhattan_dist((0, 0), (0, 1)), 1);
    assert_eq!(manhattan_dist((0, 0), (1, 1)), 2);
    assert_eq!(manhattan_dist((0, 0), (0, 0)), 0);
    assert_eq!(manhattan_dist((0, 0), (2, 4)), 6);

    assert_eq!(manhattan_dist((2, 4), (0, 0)), 6);
    assert_eq!(manhattan_dist((2, 4), (4, 2)), 4);
}

