function construct(string){
    let person = {
        name: string,
        material: "human",
        assemble: true,
        duration: 1000
    };
    return person;
}

const somePerson = construct('Kevin');
console.log('name is: ' + somePerson.name); // should be "Kevin"
console.log('duration is: ' + somePerson.duration); // should be 1000