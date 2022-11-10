use num::pow;

fn compute_sequence(target: u64) -> Vec<u64> {
    let mut num: u64 = 0;
    let mut result: Vec<u64> = Vec::with_capacity((target + 1) as usize);
    result.push(0);
    let mut inventory: Vec<u64> = vec![0u64; (target + 1) as usize];
    inventory[0] = 1;
    for _ in 2..(target + 1) {
        let c = inventory[num as usize];
        num = if c == 0 {0} else {num + 1};
        result.push(c);
        inventory[c as usize] += 1;
    }
    return result;
}

fn main() {
    println!("{:?}", compute_sequence(pow(10, 9)));
}
