# HydroGAN

## TODO
* Investigate why VAE is not producing any hydrogen masses? (Probably an issue with the decoder part of the VAE)
    * In the decode() of the VAE class, create multiple checkpoints: sum all the values in the **out** variable and plot the evolution of the sum. Compare with the sum of the input subcubes.
* GAN
    * ~~Plotting the evolution of the Generator(noise) subcubes during training~~
    * Check whether the inputs are in the range of (-1,1) -> https://github.com/soumith/ganhacks
    * We don't have any downsampling/upsampling components in both the discriminator and the generator, maybe try those (Downsampling : Average Pooling, Upsampling: PixelShuffle) -> https://github.com/soumith/ganhacks
    * Try Label smoothing? -> https://github.com/soumith/ganhacks
    * Add script to check norms of gradients - if they are over 100 things are screwing up - https://github.com/soumith/ganhacks 
* Hybrid Models
    * https://github.com/soumith/ganhacks -> if you cant use DCGANs and no model is stable, use a hybrid model : KL + GAN or VAE + GAN
    * How to use VAE + GAN?



## Data
sample data is in data folder where a .h5 file is put. sample_32.h5 is 32 of randomly sampled cubes with dimensions ?x?x?

