use md5;

fn mine(contents: String) {
    let maxiter = 100_000_000;

    for i in 1..maxiter {

        let combined = format!("{}{}", contents, i);
        let digest = md5::compute(combined);
        let hex = format!("{:x}", digest);

        if hex.starts_with("00000") {
            println!("Found at {i}");
            println!("MD5 hash: {:x}", &digest);
            return;
        }

    }

    println!("Terminated after reaching max iterations.");
}


fn main() {
    // No input file, just the following string
    let contents = String::from("yzbqklnj");
    mine(contents);
}


#[test]
fn example1() {
    let contents = String::from("abcdef");
    mine(contents);
}


#[test]
fn example2() {
    let contents = String::from("pqrstuv");
    mine(contents);
}
