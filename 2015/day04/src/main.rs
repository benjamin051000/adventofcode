fn mine(contents: &String, condition: &str) -> Result<i32, &'static str> {
    let maxiter = 10_000_000;

    for i in 1..maxiter {

        let combined = format!("{}{}", contents, i);
        let digest = md5::compute(combined);
        let hex = format!("{:x}", digest);

        if hex.starts_with(condition) {
            println!("Found MD5 hash: {:x}", &digest);
            return Ok(i);
        }

    }

    Err("Terminated after reaching max iterations.")
}


fn main() {
    // No input file, just the following string
    let contents = String::from("yzbqklnj");

    let part1 = mine(&contents, "00000").unwrap();
    println!("Part 1: {}", part1);

    let part2 = mine(&contents, "000000").unwrap();
    println!("Part 2: {}", part2);
}


#[test]
fn example1() {
    let contents = String::from("abcdef");
    let result = mine(&contents, "00000").unwrap();
    assert!(result == 609043);
}


#[test]
fn example2() {
    let contents = String::from("pqrstuv");
    let result = mine(&contents, "00000").unwrap();
    assert!(result == 1048970);
}
