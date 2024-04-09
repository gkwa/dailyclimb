const Ajv = require('ajv');
const schema = require('./person.schema.json');
const data = require('./person.json');

const ajv = new Ajv();
const validate = ajv.compile(schema);

const valid = validate(data);

if (valid) {
 console.log('JSON data is valid!');
} else {
 console.log('JSON data is invalid:', validate.errors);
}
