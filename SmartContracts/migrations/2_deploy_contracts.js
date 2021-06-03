const Sample = artifacts.require("SampleContract");

module.exports = function (deployer) {
  deployer.deploy(Sample);
};
